import subprocess
import time

while True:
    subprocess.call(["python", "/home/pi/Final/collect.py"])
    time.sleep(2)