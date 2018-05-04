import gps as GPS
import gsm as GSM
import bmp180 as BMP

numar = "+40757876350"
maxAltitude = 1000 #metri

GPSData = GPS.readDataDecimal()
BMPData = BMP.readData()
BMPAlt  = BMP.pres2alt(BMPData[1]*100)

print BMPAlt

if GPSData[2] != None:
    if GPSData[2] < maxAltitude:
        d1 = GPSData
        s = str(d1[0]) + ", " + str(d1[1]) + ", " + str(d1[2])
        GSM.sendSMS(numar, str(GPSData))
else:
    d1 = GPS.getLastLocation()
    d2 = GPS.getLastLocationDecimal()
    
    if BMPAlt < maxAltitude:
        s  = str(d1[0]) + ", " + str(d1[1]) + "\n"
        s += str(d2[0]) + ", " + str(d2[1]) + ", "
        s += str(int(BMPAlt))
        GSM.sendSMS(numar, str(s))
    