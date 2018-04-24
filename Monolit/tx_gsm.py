import sys
import time
import difflib
import pigpio

TX=27

try:
        pi = pigpio.pi()
        pi.set_mode(TX, pigpio.OUTPUT)
        pi.wave_clear()
        pi.wave_add_serial(TX, 9600, sys.argv[1]+"\r\n")
        wid=pi.wave_create()

        pi.wave_send_once(wid)   # transmit serial data
        pi.wave_delete(wid)
        time.sleep(1)

except:
        pi.stop()
