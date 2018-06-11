#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import geturlsource as URL
import urllib2
from datetime import datetime

lastTime = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')

def u2a(data):
    asciidata=data.encode("ascii","ignore")
    return asciidata
def parseData():
    callsign = "YO8BCA-11"
    
    
    s = URL.getSource("https://aprs.fi/info/?call=" + callsign)
    raw_decoded = URL.getSource("https://aprs.fi/?c=raw&call=" + callsign + "&limit=2&view=decoded")
    
    deg = unicode("°C", "utf-8")
    deg2 = unicode("°", "utf-8")
    
    regex = r'wx:<br />([^"]+)'
    
    weather = re.findall(regex, raw_decoded)
    
    lat = re.findall("latitude: (.*)" + deg2, raw_decoded)[0]
    lng = re.findall("longitude: (.*)" + deg2, raw_decoded)[0]
    lat = round(float(lat[:-1]),4)
    lng = round(float(lng[:-1]),4)
    
    try:
        weather = str(weather[0])
        weather = unicode(weather, "utf-8")
        
        pre = r'pressure:([^"]+)mbar'
        hre = r'humidity:([^"]+)%<br'
        tre = r'temp:([^"]+)' + deg
        
        press = re.findall(pre, weather)
        press = float(press[0])
        
        temp  = re.findall(tre, weather)
        temp  = float(temp[0])
        
        humid = re.findall(hre, weather)
        humid = float(humid[0])*10
        
    except:
        press = -1
        temp  = -1
        humid = -1
    
    altit = 0
    result  = re.search('Altitude:</th> <td valign=\'top\'>(.*)m</td></tr>', s)
    if result != None:
        result  = str(result.group(1))
        result  = result[:-2]
        altit   = int(result)
    
    
    result  = re.search('Comment:</th> <td valign=\'top\'><i>(.*)</i>', s)
    result  = str(result.group(1))
    comment = u2a(result)
    comment = comment.split(";")

    ts1     = float(comment[1].replace("TS",  " "))
    ts2     = float(comment[2])
    ds      = float(comment[3].replace("DS",  " "))
    bat1    = float(comment[4].replace("BAT", " "))
    bat2    = float(comment[5])
    
    result  = re.search('Last position:</th> <td valign=\'top\'>(.*)\(<span', s)
    result  = str(result.group(1))
    timp    = result[:19]
    timp    = timp[11:]
    if altit == 0:
        global lastTime
        timp = lastTime

    return [timp, lat, lng, altit, ds, temp, press, humid, ts1, ts2, bat2, bat1]


print parseData()
    
    
