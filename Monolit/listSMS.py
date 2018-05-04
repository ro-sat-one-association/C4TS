import gsm as GSM
import sys
import time
import difflib
import pigpio

TX=27

def tx(data):
	try:
			pi = pigpio.pi()
			pi.set_mode(TX, pigpio.OUTPUT)
			pi.wave_clear()
			pi.wave_add_serial(TX, 9600, data)
			wid=pi.wave_create()
	
			pi.wave_send_once(wid)   # transmit serial data
			pi.wave_delete(wid)
			time.sleep(1)
	
	except:
			pi.stop()
		
tx("AT+CREG=1\r")	
tx("AT+CSMS=1\r")	
tx("AT+CMGF=1\r")	
tx("AT+CSCS=\"GSM\"\r")	
tx("AT+CMGL=4\r")