import sys
import time
import difflib
import pigpio

RX=22 #pin GPS

def read():
    try:
            pi = pigpio.pi()
            pi.set_mode(RX, pigpio.INPUT)
            pi.bb_serial_read_open(RX, 9600, 8)
    
            string = ""
            timp = int(time.time())
            while 1:
                    (count, data) = pi.bb_serial_read(RX)
                    if count:
                            string += str(data)
                            if (string.find("\r\n") != -1):
                                    break  
                    if (int(time.time()) - timp > 5):
                        pi.bb_serial_read_close(RX)
                        pi.stop()
                        print "TIMP DEPASIT GPS"
                        return None
                    time.sleep(1)
                    
            pi.bb_serial_read_close(RX)
            pi.stop()
            return string
            
    except:
            pi.bb_serial_read_close(RX)
            pi.stop()
            print "EXCEPTIE GPS"
#print read()