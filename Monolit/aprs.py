import serial
import time

def send(toSend):
	APRS_OK = False
	port = "/dev/ttyS0"
	ser = serial.Serial(port, 9600, timeout = 0)
	x = ser.write('<APRS>'+str(toSend))
	
	data_str = ""
	
	timeout = 5
	initTime = time.time()
	
	while True:
		data = ser.read(9999)
		if len(data) > 0:
			data_str += data
		time.sleep(0.5)
		#print data_str
		if data_str.find("TRIMIT:") != -1:
			APRS_OK = True
			break
		if time.time() - initTime > timeout:
			break
	ser.close()
	return APRS_OK
