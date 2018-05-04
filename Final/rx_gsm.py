import sys
import time
import difflib
import pigpio

RX=17

pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.bb_serial_read_open(RX, 9600, 8)


line = ""
last = "last"
fisier = "/home/pi/Final/gsm.txt"

try:
    while 1:
        (count, data) = pi.bb_serial_read(RX)
        if count:
            #print repr(data)
            #print data
            line += str(data)
            #print "linie: " + line
            if line.find("\r\n") != -1 and last is not line:
                print line
                f = open(fisier, "a+")
                f.write(line)
                f.close()
                last = line
                line = ""
            if (data == '\x00'):
                f = open(fisier, "a+")
                f.write("SHUTDOWN\n")
                f.close()
                print "SHUTDOWN"
        time.sleep(0.1)
                
except:
    pi.bb_serial_read_close(RX)
    pi.stop()
  