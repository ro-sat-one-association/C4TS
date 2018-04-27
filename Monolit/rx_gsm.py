import sys
import time
import difflib
import pigpio

RX=17

try:
        pi = pigpio.pi()
        pi.set_mode(RX, pigpio.INPUT)
        pi.bb_serial_read_open(RX, 9600, 8)

        print "DATA - SOFTWARE SERIAL:"
        while 1:
                (count, data) = pi.bb_serial_read(RX)
                if count:
                        #print repr(data)
                        print data
                        if (data == '\x00'):
                            print "SHUTDOWN"
                time.sleep(1)

except:
        pi.bb_serial_read_close(RX)
        pi.stop()
