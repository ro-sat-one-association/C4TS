#include <Arduino.h>
#include <Wire.h>

#include "config.h"
#include "afsk_avr.h"
#include "aprs.h"
#include "pin.h"
#include "power.h"

#define SLAVE_ADDRESS 0x04

#define LOAD_EEPROM

//Sends an APRS packet every...
#define SEND_TIME_SPACING 10
static APRSPacket packet;


#ifdef LOAD_EEPROM
    #include "eeprom_loader.cpp"
#endif

int number = 0;

void setup()
{  
  #ifdef LOAD_EEPROM
      loadEEPROM();
  #endif

  afsk_setup();

  analogReference(INTERNAL);

  Wire.begin(SLAVE_ADDRESS);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  

  Serial.begin(9600);
}


String textPacket = "\0";

static void doSomeWork(String text) {
  packet.aprs_send(text);

  while (afsk_flush()) {
    power_save();
  }
  
}

void loop()
{
   while(Serial.available()) {
          textPacket =  Serial.readString();
   }

    if(strstr(textPacket.c_str(), "<APRS>")){
            Serial.print("TRIMIT: ");
            textPacket.remove(0, 6);
            Serial.print(textPacket);
            Serial.print("\r\n");
            doSomeWork(textPacket);  
            textPacket = "\0"; 
    }

}

void receiveData(int byteCount){
  while(Wire.available()) {
    number = Wire.read();
    Serial.println(number);
  }
}

void sendData(){
  switch(number){
    case 1: {
      Wire.write(analogRead(A0) >> 2);
    } break;

    case 2: {
      Wire.write( ( uint16_t(analogRead(A0)) << 14) >> 14);
    } break;

    case 3: {
      Wire.write(analogRead(A1) >> 2);
    } break;

    case 4:{
      Wire.write( (uint16_t(analogRead(A1)) << 14) >> 14);
    } break;
  }
  
  Wire.write(number);
}
