import time

import camera as CAM
import bmp180 as BMP
import gps	  as GPS
import tsl	  as TSL
import batt	  as BAT
import aprs	  as APRS

from sht21 import SHT21

try:
	SHT  = SHT21(0)
except IOError, e:
	print "SHT" + str(e)
	
try: 
	SHTData = (round(SHT.read_temperature(), 2), round(SHT.read_humidity(), 2))
except IOError, e:
	print "SHT" + str(e)
except NameError, e:
	print "SHT" + str(e)


def CtoF(temperature):
	return str(int(temperature * 1.8 + 32))

try:
	BMPData = BMP.readData()
except IOError:
	print "Nu pot citi BMP-ul"

	
APRSToSend  = "=4656.32N/02623.56EO" #locatie temporara pana bag GPS
APRSToSend += "c...s...g...t"

if int(CtoF(BMPData[0])) >= 0:
	if int(CtoF(BMPData[0])) < 100:
		APRSToSend += "0"
		if int(CtoF(BMPData[0])) < 10:
			APRSToSend += "0"
	APRSToSend += CtoF(BMPData[0])	
else:
	if int(CtoF(BMPData[0])) > -10:
		APRSToSend += "-0"
		APRSToSend += str(-int(CtoF(BMPData[0])))
	else:
		APRSToSend += CtoF(BMPData[0])	

	
APRSToSend += "h"
	
APRSToSend += str(int(SHTData[1]))

APRSToSend += "b" #cand o sa fie adaugat SHT21

tailingZeros = 5 - len(str(int(BMPData[1]*10)))
for i in range(tailingZeros):
	APRSToSend += "0"	
if tailingZeros < 0:
	APRSToSend += "....."
else:
	APRSToSend += str(int(BMPData[1]*10))
	
APRSToSend += "TEST"

print APRS.send(APRSToSend)

print APRSToSend