#include "config.h"
#include "ax25.h"
#include "aprs.h"
#include <stdio.h>
#include <stdlib.h>

#if (ARDUINO + 1) >= 100
#  include <Arduino.h>
#else

#  include <WProgram.h>

#endif


// // Module functions
// float meters_to_feet(float m) {
//     // 10000 ft = 3048 m
//     return m / 0.3048;
// }


APRSPacket::APRSPacket(){}


void APRSPacket::aprs_send(String input) {

    const struct s_address addresses[] = { 
      {D_CALLSIGN, D_CALLSIGN_ID},  // Destination callsign
      {S_CALLSIGN, S_CALLSIGN_ID},  // Source callsign (-11 = balloon, -9 = car)
      {DIGI_PATH1, DIGI_PATH1_TTL}, // Digi1 (first digi in the chain)
    }; 

    char sep = '/';
/*
    ax25_send_header(addresses, sizeof(addresses) / sizeof(s_address));
    ax25_send_byte('@');                // Symbol table
    ax25_send_string(this->datetime);         // 170915 = 17h:09m:15s zulu (not allowed in Status Reports)
    ax25_send_byte('h');               // Report w/ timestamp, no APRS messaging. $ = NMEA raw data
    ax25_send_byte(sep);                // Symbol table
    ax25_send_string(this->latitude);     // Lat: 38deg and 22.20 min (.20 are NOT seconds, but 1/100th of minutes)             
    ax25_send_string(this->longitude);     // Lon: 000deg and 25.80 min
    ax25_send_byte('>');                // Symbol: O=balloon, -=QTH

    ax25_send_byte(this->heading);             // Course (degrees)
    ax25_send_byte(this->speed);             // speed (knots)
    ax25_send_byte('I');

    ax25_send_string("A=");                     // Altitude (feet). Goes anywhere in the comment area
    ax25_send_string(this->altitude);
    ax25_send_byte(sep);

    ax25_send_string("Ti=");
    ax25_send_string(this->intTemp);
    ax25_send_byte(sep);

    ax25_send_string("P=");
    ax25_send_string(this->pressure);

    ax25_send_string(" TEST mariocaster@gmail.com");     // Comment

    ax25_send_footer();

    ax25_flush_frame();                 // Tell the modem to go */



    //ax25_send_header(addresses, sizeof(addresses) / sizeof(s_address));
  //  ax25_send_byte('@');                // Symbol table
    //ax25_send_string(this->datetime);         // 170915 = 17h:09m:15s zulu (not allowed in Status Reports)
    //ax25_send_byte('h');               // Report w/ timestamp, no APRS messaging. $ = NMEA raw data
    //ax25_send_byte(sep);                // Symbol table
    //ax25_send_string(this->latitude);     // Lat: 38deg and 22.20 min (.20 are NOT seconds, but 1/100th of minutes)             
    //ax25_send_string(this->longitude);     // Lon: 000deg and 25.80 min
    //ax25_send_byte('>');                // Symbol: O=balloon, -=QTH

   // ax25_send_byte(this->heading);             // Course (degrees)
    //ax25_send_byte(this->speed);             // speed (knots)
    //ax25_send_byte('I');

    //ax25_send_string("A=");                     // Altitude (feet). Goes anywhere in the comment area
    //ax25_send_string(this->altitude);
    //ax25_send_byte(sep);
    

    ax25_send_header(addresses, sizeof(addresses) / sizeof(s_address));

    ax25_send_string(input.c_str());
    
    //ax25_send_string(" TEST pascues");     // Comment

    ax25_send_footer();

    ax25_flush_frame();                 // Tell the modem to go 

    
}
