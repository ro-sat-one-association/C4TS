#!/usr/bin/python
import os
import sys
import subprocess
import time
import datetime
from subprocess import call
from find_usb import findUSB
name       = "V"
number     = 0
extenstion = ".h264"
time_sec   = 300 #default time in seconds
fps        = 30

dev_number   = 1
usb_dev      = findUSB()
mount_folder = "USB"

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        sys.exit("Prea multe argumente")
    else:
        time_sec = int(sys.argv[1])
        
if usb_dev is None:
    sys.exit("N-am gasit niciun USB / Sunt mai multe") #I haven't found any USB device / there are more
else:
    output = subprocess.check_output(["mount", usb_dev + str(dev_number), mount_folder])

while True:
    timp = time.time()
    timestamp = datetime.datetime.fromtimestamp(timp).strftime('%H-%M-%S__%d-%m-%Y')
    
    nume = name + str(number) + '_' + timestamp + extenstion
    
    call(["raspivid", "-o", nume, "-t", str(time_sec*1000), "-fps", str(fps), ])
    #call(["mv", name + str(number) + extenstion, "Move" ])
    os.system("nohup mv " + nume + ' ' + mount_folder + " &")
    number = number + 1
