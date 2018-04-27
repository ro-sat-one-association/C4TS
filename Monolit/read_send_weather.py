import time

import camera as CAM
import bmp180 as BMP
import gps	  as GPS
import tsl	  as TSL
import batt	  as BAT
import aprs	  as APRS
import check  as CHECK

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
	if (CHECK.GPS_OK == False):
		GPSData = GPS.getLastLocation()
except:
	print "Nu pot citi GPS-ul"
	GPSData = GPS.getLastLocation()

APRS1   = "="
APRS1  += GPSData[0]
APRS1  += "/" #indicator tabel
APRS1  += GPSData[1]
APRS1  += "_" #_ - wx O - balon
#APRS1  = "=4656.32N/02623.56E_" 
APRS1 += "c...s...g...t"


###TEMPERATURA BMP###
if int(CtoF(BMPData[0])) >= 0:
	if int(CtoF(BMPData[0])) < 100:
		APRS1 += "0"
		if int(CtoF(BMPData[0])) < 10:
			APRS1 += "0"
	APRS1 += CtoF(BMPData[0])	
else:
	if int(CtoF(BMPData[0])) > -10:
		APRS1 += "-0"
		APRS1 += str(-int(CtoF(BMPData[0])))
	else:
		APRS1 += CtoF(BMPData[0])	
#####################


###UMIDITATE SHT###
APRS1 += "h"
APRS1 += str(int(SHTData[1]))
###################


###PRESIUNE BMP###
APRS1 += "b" 
tailingZeros = 5 - len(str(int(BMPData[1]*10)))
for i in range(tailingZeros):
	APRS1 += "0"	
if tailingZeros < 0:
	APRS1 += "....."
else:
	APRS1 += str(int(BMPData[1]*10))
##################	

print APRS.send(APRS1)
print APRS1

time.sleep(3)


APRS2   = "="
APRS2  += GPSData[0]
APRS2  += "/" #indicator tabel
APRS2  += GPSData[1]
APRS2  += "O" #_ - wx O - balon 
APRS2  += CHECK.getAPRS()
APRS2 += "/A="
APRS2 += GPS.getAltitudeAPRS(GPSData[2])

print APRS.send(APRS2)

print APRS2