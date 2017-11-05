#include <Arduino.h>
#include "config.h"
#include "afsk_avr.h"
#include "aprs.h"
#include "pin.h"
#include "power.h"
#include <string.h>

char FLAGAPRS[] = "<APRS>";
char FLAGGPRS[] = "<GPRS>";

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
        }
          
        if(strstr(textPacket.c_str(), FLAGAPRS)){
              
              Serial.print("TRIMIT: ");
              textPacket.remove(0, 6);
             // textPacket.trim();

              Serial.print(textPacket);
              Serial.print("\r\n");
              
              packet.aprs_send(textPacket);
             // while (afsk_flush()) {power_save();}
        }

        if(strstr(textPacket.c_str(), FLAGGPRS)){
              
              textPacket.remove(0, 6);
              textPacket.trim();
              
              Serial.print(textPacket);
              Serial.print("\r\n");
              
        }
  
}
