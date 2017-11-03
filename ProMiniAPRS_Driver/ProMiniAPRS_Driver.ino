#include <Arduino.h>
#include "config.h"
#include "afsk_avr.h"
#include "aprs.h"
#include "pin.h"
#include "power.h"
#include <string.h>

char FLAG[] = "<APRS>";

static APRSPacket packet;
String textPacket = "\0";


void setup()
{  

  afsk_setup();
  Serial.begin(9600);

}


void loop()
{ 
        while(Serial.available()) {
          textPacket =  Serial.readString();
          Serial.println(textPacket);
        }

        if (textPacket[0]!= '\0'){
          if(strstr(textPacket.c_str(), FLAG)){
              
              Serial.print("TRIMIT: ");
              textPacket.remove(0, 6);
              textPacket.trim();

              Serial.println(textPacket);

              
              packet.aprs_send(textPacket);
              while (afsk_flush()) {power_save();}
          }
          textPacket[0] = '\0';   
        }

  
}
