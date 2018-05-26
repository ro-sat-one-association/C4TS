#include <Arduino.h>

#define SLAVE_ADDRESS 0x04

#include <Wire.h>

#include "config.h"
#include "afsk_avr.h"
#include "aprs.h"
#include "pin.h"
#include "power.h"


#define LOAD_EEPROM

static uint8_t next_aprs = 0;


#define SEND_TIME_SPACING 10

static APRSPacket packet;
String textPacket = "\0";

#ifdef LOAD_EEPROM
    #include "eeprom_loader.cpp"
#endif

int number = 0;

void setup()
{  
  #ifdef LOAD_EEPROM
      loadEEPROM();
  #endif

  analogReference(INTERNAL);

  Wire.begin(SLAVE_ADDRESS);

  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(9600);
  pinMode(4, OUTPUT);

  afsk_setup();

}

static void doSomeWork(String text) {
  packet.aprs_send(text);

  while (afsk_flush()) {
    power_save();
  }
  
} // doSomeWork


void loop()
{

   while(Serial.available()) {
      textPacket =  Serial.readString();
    }

    if(strstr(textPacket.c_str(), "<APRS>")){  
              digitalWrite(LED_BUILTIN, HIGH);  
              delay(500);                       
              digitalWrite(LED_BUILTIN, LOW);  
              delay(500);  

              digitalWrite(4, HIGH);
              
              Serial.print("TRIMIT: ");
              textPacket.remove(0, 6);
             // textPacket.trim();

              Serial.print(textPacket);
              Serial.print("\r\n");
              
              doSomeWork(textPacket);
              
              digitalWrite(4, LOW);
              textPacket = "\0";
             // while (afsk_flush()) {power_save();}
        }
     digitalWrite(LED_BUILTIN, LOW);  
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
  
  //Wire.write(number);
}

