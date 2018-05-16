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
    callsign = "YO8RTZ-10"
    
    
    s = URL.getSource("https://aprs.fi/info/?call=" + callsign)
    raw_decoded = URL.getSource("https://aprs.fi/?c=raw&call=" + callsign + "&limit=2&view=decoded")
    
    deg = unicode("°C", "utf-8")
    
    regex = r'wx:<br />([^"]+)'
    
    weather = re.findall(regex, raw_decoded)
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
    
    status   = comment[0]
    status   = status.split("Ba")
    statusBa = status[1]
    status   = status[0]
    
    status   = status.split("S")
    statusS  = status[1]
    status   = status[0]
    
    status   = status.split("T")
    statusT  = status[1]
    status   = status[0]
    
    status   = status.split("D")
    statusD  = status[1]
    status   = status[0]
    
    status   = status.split("G")
    statusG  = status[1]
    status   = status[0]
    
    status   = status.split("B")
    statusB  = status[1]
    
    ts1     = float(comment[1].replace("TS",  " "))
    ts2     = float(comment[2])
    ds      = float(comment[3].replace("DS",  " "))
    bat1    = float(comment[4].replace("BAT", " "))
    bat2    = float(comment[5])
    
    result  = re.search('Last position:</th> <td valign=\'top\'>(.*)\(<span', s)
    result  = str(result.group(1))
    timp    = result[:19]
    timp    = datetime.strptime(timp, '%Y-%m-%d %H:%M:%S')
    if altit == 0:
        global lastTime
        timp = lastTime
    
    return [ds, temp, press, humid, altit, ts1, ts2, bat2, bat1, statusBa, statusS, statusT, statusD, statusG, statusB, timp]


def submitData():
    global lastTime
    data = parseData()
    if data[15] > lastTime:
        if data[1] != -1: #T ext
            u = urllib2.urlopen("http://localhost/submit.php?table=1&v1=" + str(data[0]) + "&v2=" + str(data[1]))
            u.close()
            
        if data[2] != -1 and data[3] != -1: #pressure
            u = urllib2.urlopen("http://localhost/submit.php?table=2&v1=" + str(data[2]) + "&v2=" + str(data[3]))
            u.close()  
            u = urllib2.urlopen("http://localhost/submit.php?table=3&v1=" + str(data[2]) + "&v2=" + str(data[4]))
            u.close()
            
        u = urllib2.urlopen("http://localhost/submit.php?table=4&v1=" + str(data[5]) + "&v2=" + str(data[6]))
        u.close()
        u = urllib2.urlopen("http://localhost/submit.php?table=5&v1=" + str(data[7]) + "&v2=" + str(data[8]))
        u.close()
        u = urllib2.urlopen("http://localhost/submit.php?table=GPS&v1=" + str(data[13]))
        u.close()
        
        lastTime = data[15]
        print data

while True:
    submitData()
    time.sleep(10)
    
    
    
