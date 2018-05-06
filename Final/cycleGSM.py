import subprocess
import time

while True:
    subprocess.call(["python", "/home/pi/Final/sendCoord.py"])
    #subprocess.call(["python", "/home/pi/Final/sendAPRS.py"])
    time.sleep(120)
