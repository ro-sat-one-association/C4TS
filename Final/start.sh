#!/bin/sh
sudo pigpiod
gpio mode 1 output
gpio write 1 1
rm /home/pi/Final/gsm.txt
#rm /home/pi/Final/MPU.txt
python /home/pi/Final/rx_gsm.py &
python /home/pi/Final/stopGSM.py &
python /home/pi/Final/Fusion10.py &
/home/pi/Final/main &

