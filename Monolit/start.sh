#!/bin/sh
sudo pigpiod
gpio mode 1 output
gpio write 1 1
rm /home/pi/Coduri/Monolit_dev/gsm.txt
python /home/pi/Coduri/Monolit_dev/rx_gsm.py &
