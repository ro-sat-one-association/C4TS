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

    ax25_send_header(addresses, sizeof(addresses) / sizeof(s_address));

    ax25_send_string(input.c_str());
    
    ax25_send_footer();

    ax25_flush_frame();                 // Tell the modem to go
}
