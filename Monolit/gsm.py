import sys
import time
import difflib
import pigpio
import subprocess

TX  = 27
RX  = 17

subprocess.call(["gpio", "mode", "1", "output"])
subprocess.call(["gpio", "write", "1", "1"])

def write(state):
	subprocess.call(["gpio", "write", "1", str(state)])

def Tx(data):
	try:
			pi = pigpio.pi()
			pi.set_mode(TX, pigpio.OUTPUT)
			pi.wave_clear()
			pi.wave_add_serial(TX, 9600, data+"\r\n")
			wid=pi.wave_create()
	
			pi.wave_send_once(wid)   # transmit serial data
			pi.wave_delete(wid)
	
	except:
			pi.stop()

def	Rx():
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
                    if (int(time.time()) - timp > 2):
                        pi.bb_serial_read_close(RX)
                        pi.stop()
                        print "TIMP DEPASIT GSM"
                        return None
                    time.sleep(1)
                    
            pi.bb_serial_read_close(RX)
            pi.stop()
            return string
            
    except:
            pi.bb_serial_read_close(RX)
            pi.stop()
            print "EXCEPTIE GSM"			

def StartStop():
	write(0)
	time.sleep(2)
	write(1)
	
def isAlive():
	Tx("AT")
	output = Rx()
	if (str(output).find("OK") != -1):
		return True
	return False
