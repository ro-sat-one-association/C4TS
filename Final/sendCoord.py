import gps as GPS
import gsm as GSM
import bmp180 as BMP
import time

numar = "+40757876350"
maxAltitude = 700 #metri

GPSData = GPS.readDataDecimal()

try:
    BMPData = BMP.readData()
    BMPAlt  = BMP.pres2alt(BMPData[1]*100)
except:
    BMPData = [-1, -1]
    BMPAlt  = 0
    
print BMPAlt

f    = open("/home/pi/Final/OK_GSM.txt", "r")
s    = f.read()
f.close()

s    = s.split(" ")
ok   = s[0]
timp = float(s[1])


if GPSData[2] != None:
    if GPSData[2] < maxAltitude:
        if ok == "0":
            d1 = GPSData
            s = str(d1[0]) + ", " + str(d1[1]) + ", " + str(d1[2])
            GSM.sendSMS(numar, str(s))
            
        elif time.time() - timp >= (60 * 10):
            d1 = GPSData
            s = str(d1[0]) + ", " + str(d1[1]) + ", " + str(d1[2])
            GSM.sendSMS(numar, str(s))
            
        f = open("/home/pi/Final/OK_GSM.txt", "w")  
        f.write("1 " + str(time.time()))
        f.close()
        
    else:
        f = open("/home/pi/Final/OK_GSM.txt", "w")  
        f.write("0 0")
        f.close()
        
else:
    d1 = GPS.getLastLocation()
    d2 = GPS.getLastLocationDecimal()
    
    if BMPAlt < maxAltitude:
        if ok == "0":
            s  = str(d1[0]) + ", " + str(d1[1]) + "\n"
            s += str(d2[0]) + ", " + str(d2[1]) + ", "
            s += str(int(BMPAlt))
            GSM.sendSMS(numar, str(s))
            
        elif time.time() - timp >= (60 * 10):
            s  = str(d1[0]) + ", " + str(d1[1]) + "\n"
            s += str(d2[0]) + ", " + str(d2[1]) + ", "
            s += str(int(BMPAlt))
            GSM.sendSMS(numar, str(s))
            
        f = open("/home/pi/Final/OK_GSM.txt", "w")  
        f.write("1 " + str(time.time()))
        f.close()
    else:
        f = open("/home/pi/Final/OK_GSM.txt", "w")  
        f.write("0 0")
        f.close()
    
