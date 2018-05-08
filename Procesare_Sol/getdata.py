#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import time

def u2a(data):
    asciidata=data.encode("ascii","ignore")
    return asciidata
def parseData():
    callsign = "YO8RTZ-10"
    response = urllib2.urlopen("https://aprs.fi/info/?call=" + callsign)
    page_source = response.read()
    #s = unicode(page_source, "utf-8")
    s = page_source
    
    deg = unicode("°C", "utf-8")
    
    
    #result  = re.search('/>(.*)mbar', s)
    #result  = str(result.group(1))
    #weather = unicode(result, "utf-8")
    weather = "-1.1 °C 45% 950.2"
    weather = unicode(weather, "utf-8")
    weather = weather.split(deg)
    temp1   = weather[0]
    humid   = (weather[1].split("%"))[0]
    press   = (weather[1].split("%"))[1]
    
    temp1   = float(u2a(temp1))
    humid   = int(u2a(humid))*100
    press   = float(u2a(press))*10
    
    result  = re.search('Altitude:</th> <td valign=\'top\'>(.*)m</td></tr>', s)
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
    return [ds, ts1, press, altit, ts1, ts2, bat2, bat1, statusBa, statusS, statusT, statusD, statusG, statusB]

def submitData():
    data = parseData()
    urllib2.urlopen("http://localhost/submit.php?table=1&v1=" + str(data[0]) + "&v2=" + str(data[1]))
    urllib2.urlopen("http://localhost/submit.php?table=2&v1=" + str(data[3]) + "&v2=" + str(data[4]))
    urllib2.urlopen("http://localhost/submit.php?table=3&v1=" + str(data[3]) + "&v2=" + str(data[5]))
    urllib2.urlopen("http://localhost/submit.php?table=4&v1=" + str(data[6]) + "&v2=" + str(data[7]))
    urllib2.urlopen("http://localhost/submit.php?table=5&v1=" + str(data[8]) + "&v2=" + str(data[9]))

while True:
    submitData()
    time.sleep(1)
    
