#!/bin/sh
sudo pigpiod
gpio mode 1 output
gpio write 1 1
rm /home/pi/Final/gsm.txt
#rm /home/pi/Final/MPU.txt
/home/pi/Final/MPU9250 &
python /home/pi/Final/rx_gsm.py &
python /home/pi/Final/stopGSM.py
