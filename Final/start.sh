#!/bin/sh
sudo pigpiod
gpio mode 1 output
gpio write 1 1
rm /home/pi/Final/gsm.txt
rm /home/pi/Final/OK_GSM.txt
echo 0 0 > /home/pi/Final/OK_GSM.txt
python /home/pi/Final/rx_gsm.py &
python /home/pi/Final/stopGSM.py &
/home/pi/Final/main &

