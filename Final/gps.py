import rx_gps as GPS_RX
import pynmea2

def readData():
    data = GPS_RX.read()
    data = str(GPS_RX.read())
    data = data.split('\n')
    GGA  = ""
    
    for i in range(0, len(data)):
        if (data[i].find("GGA") != -1):
            GGA = data[i]
            break
    try:
        msg = pynmea2.parse(GGA)
    except ParseError:
        return [0,0, None]
    lat_dec  = msg.latitude
    long_dec = msg.longitude
    altitude = msg.altitude
    
    lat =  int(lat_dec) * 100
    lat += int((lat_dec - int(lat_dec))*60)
    lat += (lat_dec - int(lat_dec))*60 - int((lat_dec - int(lat_dec))*60)
    lat =  '%.2f' % round(lat,2)
    
    if lat_dec > 0:
        lat = str(lat) + "N"
    else:
        lat = str(lat) + "S"
    
    long  =  int(long_dec) * 100
    long += int((long_dec - int(long_dec))*60)
    long += (long_dec - int(long_dec))*60 - int((long_dec - int(long_dec))*60)
    long  = '%.2f' % round(long,2)
    
    if long_dec > 0:
        long = str(long) + "E"
        if long_dec < 100:
            long = "0" + long
    else:
        long = str(long) + "W"
        if long_dec > -100:
            long = "0" + long
    
    if altitude != None:
        f = open('gps.txt', 'w')
        data = str(lat) + "," + str(long) + "," + str(altitude)
        f.write (data)
        f.close()
    return [lat,long,altitude]

def readDataDecimal():
    data = GPS_RX.read()
    data = str(GPS_RX.read())
    data = data.split('\n')
    GGA  = ""
    
    for i in range(0, len(data)):
        if (data[i].find("GGA") != -1):
            GGA = data[i]
            break
    
    try:
        msg = pynmea2.parse(GGA)
    except ParseError:
        return [0,0, None]
    
    lat  = msg.latitude
    long = msg.longitude
    altitude = msg.altitude
    if altitude != None:
        f = open('gps_dec.txt', 'w')
        data = str(lat) + "," + str(long) + "," + str(altitude)
        f.write (data)
        f.close()
        
    return [lat,long,altitude] 
    
def getLastLocation():
    f = open('/home/pi/gps.txt', 'r')
    GPSStr = f.read()
    f.close()
    GPSData = GPSStr.split(',')
    return GPSData
    
def getLastLocationDecimal():
    f = open('/home/pi/gps_dec.txt', 'r')
    GPSStr = f.read()
    f.close()
    GPSData = GPSStr.split(',')
    return GPSData
    