import time
from datetime import datetime

import bmp180 as BMP
import gps    as GPS
import tsl    as TSL
import batt   as BAT

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

f = open("/home/pi/Date.txt", "a")
   
BMP_OK      = False
GPS_OK      = False
DS18_OK     = False
TSL_OK      = False
SHT_OK      = False
BAT_OK      = False

BMPData  = [-1, -1]
GPSData  = [-1, -1, None]
DS18Data = -1
TSLData  = [-1, -1]
SHTData  = [-1, -1]
BATData  = [-1, -1]

try:
    BMPData = BMP.readData()
    BMP_OK  = True
except IOError, e:
    print "BMP" + str(e)
    
try:
    GPSData = GPS.readData()
    if (GPSData[2] != None):
        GPS_OK  = True
    else:
        GPSData = GPS.getLastLocation()
except:
    print "Nu pot citi GPS-ul"
    GPSData = GPS.getLastLocation()
    
try:
    DS18Data = DS18.readTemperature()
    if (DS18Data != -1):
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

stateString  = ""
stateString += "BMP:"  + str(BMP_OK)  + " " +  str(BMPData)  + "\n"
stateString += "GPS:"  + str(GPS_OK)  + " " +  str(GPSData)  + "\n"
stateString += "DS18:" + str(DS18_OK) + " " +  str(DS18Data) + "\n"
stateString += "TSL:"  + str(TSL_OK)  + " " +  str(TSLData)  + "\n"
stateString += "SHT:"  + str(SHT_OK)  + " " +  str(SHTData)  + "\n"
stateString += "BAT:"  + str(BAT_OK)  + " " +  str(BATData)  + "\n"

APRSToSend  = ""
APRSToSend += "B"  +  str(int(BMP_OK ))
APRSToSend += "G"  +  str(int(GPS_OK ))
APRSToSend += "D"  +  str(int(DS18_OK))
APRSToSend += "T"  +  str(int(TSL_OK ))
APRSToSend += "S"  +  str(int(SHT_OK ))
APRSToSend += "Ba" +  str(int(BAT_OK ))

APRSToSend += ";"
APRSToSend += "TS" +  str(TSLData[0]) + ";" + str(TSLData[1]) + ";"
APRSToSend += "DS" +  str(DS18Data)   + ";"
APRSToSend += "BAT"+  str(BATData[0]) + ";" + str(BATData[1]) 


DataString =  str(BMPData[0])  + "," + str(BMPData[1]) + ","
DataString += str(GPSData[0])  + "," + str(GPSData[1]) + "," + str(GPSData[2]) + ","
DataString += str(DS18Data) + "," 
DataString += str(TSLData[0])  + "," + str(TSLData[1]) + ","
DataString += str(SHTData[0])  + "," + str(SHTData[1]) + ","
DataString += str(BATData[0])  + "," + str(BATData[1]) + "\n"


"""
BMPData  = [-1, -1]
GPSData  = [-1, -1, None]
DS18Data = -1
TSLData  = [-1, -1]
SHTData  = [-1, -1]
BATData  = [-1, -1]
"""

print stateString

f.write(str(datetime.utcnow())+"\n")
f.write(stateString + "\n\n")
f.close()


lastData = open("/home/pi/lastData.txt", "a")
lastData.write(DataString + APRSToSend + "\n")
lastData.close()

    