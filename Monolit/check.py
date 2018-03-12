import time

import camera as CAM
import bmp180 as BMP
import gps	  as GPS
import tsl	  as TSL
import batt	  as BAT
import aprs	  as APRS

from sht21 import SHT21
from ds    import DS18B20

try:
	DS18 = DS18B20()
except IOError, e:
	print "DS18" + str(e)

try:
	SHT  = SHT21(0)
except IOError, e:
	print "SHT" + str(e)

CAM_OK		= False #CAM.test()
BMP_OK		= False
GPS_OK		= False
TSL_OK		= False
BAT_OK		= False
SHT_OK		= False
DS18_OK 	= False
APRSToSend  = "=4656.32N/02623.56EO" #locatie temporara pana bag GPS

stateString = "CAM:" + str(CAM_OK) + "\n"

try:
	BMPData = BMP.readData()
	BMP_OK  = True
except IOError, e:
	print "BMP" + str(e)
	
try:
	DS18Data = DS18.readTemperature()
	DS18_OK   = True
except IOError, e:
	print "DS18" + str(e)
except NameError, e:
	print "DS18" + str(e)
	
try:
	TSLData = TSL.readData()
	TSL_OK  = True
except IOError, e:
	print "TSL" + str(e)
	
try: 
	SHTData = (round(SHT.read_temperature(), 2), round(SHT.read_humidity(), 2))
	SHT_OK  = True
except IOError, e:
	print "SHT" + str(e)
except NameError, e:
	print "SHT" + str(e)
	
try:
	BATData = BAT.readData()
	if(int(BATData[0]) > 0 and int(BATData[1]) > 0):
		BAT_OK  = True
except IOError, e:
	print "BAT" + str(e)

	
try:
	stateString += "BMP:" + str(BMP_OK)  + " " + str(BMPData)   + "\n"
except NameError:
	stateString += "BMP:" + str(BMP_OK)  + "\n"

try:
	stateString += "DS18:" + str(DS18_OK) + " " +  str(DS18Data) + "\n"
except NameError:
	stateString += "DS18:" + str(DS18_OK) + "\n"

try:
	stateString += "TSL:"  + str(TSL_OK)  + " " +  str(TSLData) + "\n"
except NameError:
	stateString += "TSL:"  + str(TSL_OK)  + "\n"

try:
	stateString += "SHT:"  + str(SHT_OK)  + " " +  str(SHTData) + "\n"
except NameError:
	stateString += "SHT:"  + str(SHT_OK)  + "\n"
	
try:
	stateString += "BAT:"  + str(BAT_OK)  + " " +  str(BATData) + "\n"
except NameError:
	stateString += "BAT:"  + str(BAT_OK)  + "\n"

	
APRSToSend += "Test"
	
stateString += "APRS: " + str(APRS.send(APRSToSend))
	
print stateString
	
