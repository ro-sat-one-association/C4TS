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
	SHTData = [0, 0]
	
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
	BMPData = [0,0]

try:
	GPSData = GPS.readData()
except:
	print "Nu pot citi GPS-ul"

APRSToSend   = "="
APRSToSend  += GPSData[0]
APRSToSend  += "/" #indicator tabel
APRSToSend  += GPSData[1]
APRSToSend  += "_" #_ - wx O - balon
#APRSToSend  = "=4656.32N/02623.56E_" 
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

APRSToSend += "b" 

tailingZeros = 5 - len(str(int(BMPData[1]*10)))
for i in range(tailingZeros):
	APRSToSend += "0"	
if tailingZeros < 0:
	APRSToSend += "....."
else:
	APRSToSend += str(int(BMPData[1]*10))
	
APRSToSend += "TEST"

print APRS.send(APRSToSend)

time.sleep(5)

print APRSToSend

APRSToSend   = "="
APRSToSend  += GPSData[0]
APRSToSend  += "/" #indicator tabel
APRSToSend  += GPSData[1]
APRSToSend  += "O" #_ - wx O - balon
APRSToSend  += "Date_etc_chestii_TEST"

print APRS.send(APRSToSend)

print APRSToSend