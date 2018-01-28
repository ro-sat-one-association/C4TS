#ifndef __APRS_H__
#define __APRS_H__

#if (ARDUINO + 1) >= 100
#  include <Arduino.h>
#else

#  include <WProgram.h>

#endif  

class APRSPacket {
    public:
    char datetime[7];
  char latitude[5];
  char longitude[5];
  char altitude[6];
  char speed;
  char heading;
  char intTemp[6];
  char pressure[6];

  void aprs_send(String input);

  //Setters

  //Constructors
  APRSPacket();
  APRSPacket(
    float _altitude,
    float _intTemp,
    int32_t _pressure);
};

#endif
