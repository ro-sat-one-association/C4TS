import serial
import time

import bmp180 as BMP
import gps	  as GPS
import tsl	  as TSL
import batt	  as BAT
import aprs	  as APRS

from ds import DS18B20
DS18 = DS18B20()

BMP_OK		= False
GPS_OK		= False
TSL_OK		= False
BAT_OK		= False
DS18_OK 	= False
APRSToSend  = "=4656.00N/02622.00EO" #locatie temporara pana bag GPS

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
	
try:
	TSLData = TSL.readData()
	TSL_OK  = True
except IOError, e:
	print "TSL" + str(e)
	
try:
	BATData = BAT.readData()
	BAT_OK  = True
except IOError, e:
	print "BAT" + str(e)
	
	
try:
	APRSToSend +=  "BMP: " + str(BMP_OK)  + " " + str(BMPData)   + "\n"
except NameError:
	APRSToSend +=  "BMP: " + str(BMP_OK)  + "\n"

try:
	APRSToSend += "DS18: " + str(DS18_OK) + " " +  str(DS18Data) + "\n"
except NameError:
	APRSToSend += "DS18: " + str(DS18_OK) + "\n"

try:
	APRSToSend += "TSL: "  + str(TSL_OK)  + " " +  str(TSLData) + "\n"
except NameError:
	APRSToSend += "TSL: "  + str(TSL_OK)  + "\n"
	
try:
	APRSToSend += "BAT: "  + str(BAT_OK)  + " " +  str(BATData) + "\n"
except NameError:
	APRSToSend += "BAT: "  + str(BAT_OK)  + "\n"

print APRSToSend
	
#print "APRS: " + str(APRS.send(APRSToSend))


	
"""
print BMP.readData()
print TSL.readData()
print BAT.readData()
"""