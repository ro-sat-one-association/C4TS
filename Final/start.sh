#!/bin/sh
sudo pigpiod
gpio mode 1 output
gpio write 1 1
rm /home/pi/Final/gsm.txt
python /home/pi/Final/rx_gsm.py &
python /home/pi/Final/stopGSM.py &
/home/pi/Final/main &

