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


APRSPacket::APRSPacket(){}

void APRSPacket::aprs_send(String input) {

    const struct s_address addresses[] = { 
      {D_CALLSIGN, D_CALLSIGN_ID},  // Destination callsign
      {S_CALLSIGN, S_CALLSIGN_ID},  // Source callsign (-11 = balloon, -9 = car)
      {DIGI_PATH1, DIGI_PATH1_TTL}, // Digi1 (first digi in the chain)
    }; 

    ax25_send_header(addresses, sizeof(addresses) / sizeof(s_address));
    
    ax25_send_string(input.c_str());
    
   // ax25_send_string("&C4TS in space");    // Comment

    ax25_send_footer();

    ax25_flush_frame();                 // Tell the modem to go
       
    //ax25_send_string("YO8RTZ-11>APRS:");
    //ax25_send_string("!4656.63NR02621.20E");
    //ax25_send_string("_000/000g000t039h50b09900");
    
}
