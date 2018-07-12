#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import geturlsource as URL
import urllib2
from upload_habitat import upload_habitat
from datetime import datetime



lastTime = datetime.strptime("2000-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')

def u2a(data):
    asciidata=data.encode("ascii","ignore")
    return asciidata
def parseData():
    callsign = "YO8BCA-11"
    
    s = URL.getSource("https://aprs.fi/?c=raw&call=" + callsign + "&limit=2&view=normal")
    
    regex = r'<div class=\'browselist_data\'>([^"]+)'
    
    result = re.findall(regex, s)
    
    result  = result[0]
    
    result = result.split('\n')
   
    
    unu = False
    doi = False
    data = False
    
    for s in result:
        timp = lastTime
        
        if s.find("...") != -1:
            temp  = s.split("...t")[1][0:3]
            temp  = round(((float(temp) - 32) * 5.0 / 9.0), 2)
            humid = float(s.split("h")[4][0:2]) * 10
            press = float(s.split("b")[3][0:5])/10
            unu = True
        
        if s.find("OB") != -1:
            statusB = s.split("OB")[1][0:1]
            statusG = s.split("G")[1][0:1]
            statusD = s.split("D")[2][0:1]
            statusT = s.split("T")[2][0:1]
            statusS = s.split("S")[5][0:1]
            statusBa = s.split("Ba")[1][0:1]
            
            ts1 = s.split("TS")[1].split(";")[0]
            ts2 = s.split("TS")[1].split(";")[1]
            
            bat1 = float(s.split("BAT")[1].split(";")[0])
            bat2 = float(s.split("BAT")[1].split(";")[1].split("/")[0])
            
            ds = s.split("DS")[1].split(";")[0] 
            
            altit = int((float(s.split("A=")[1][0:6]) * 0.3048))
            
            timp = s.split("raw_line'>")[1][0:19]
            timp    = datetime.strptime(timp, '%Y-%m-%d %H:%M:%S')
            
            doi = True
        
        if unu and doi:  
            data = [ds, temp, press, humid, altit, ts1, ts2, bat2, bat1, statusBa, statusS, statusT, statusD, statusG, statusB, timp]
            break
            
    return data
            

def submitData():
    global lastTime
    data = parseData()
    
    if data != False:
    
        pass_script = "pass"
        host        = "localhost"
        
        if data[15] > lastTime:
            print upload_habitat()
            if data[1] != -1: #T ext
                u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=1&v1=" + str(data[0]) + "&v2=" + str(data[1]))
                u.close()
                
            if data[2] != -1 and data[3] != -1: #pressure
                u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=2&v1=" + str(data[2]) + "&v2=" + str(data[3]))
                u.close()  
                u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=3&v1=" + str(data[2]) + "&v2=" + str(data[4]))
                u.close()
                
            if data[5] != -1 and data[6] != -1:    
                u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=4&v1=" + str(data[5]) + "&v2=" + str(data[6]))
                u.close()
            if data[7] != -1 and data[8] != -1:
                u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=5&v1=" + str(data[7]) + "&v2=" + str(data[8]))
                u.close()
    
            
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=GPS&v1=" + str(data[13]))
            u.close()
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=SHT&v1=" + str(data[10]))
            u.close()
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=TSL&v1=" + str(data[11]))
            u.close()
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=DS18&v1=" + str(data[14]))
            u.close()
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=BMP&v1=" + str(data[12]))
            u.close()
            u = urllib2.urlopen("http://" + host + "/submit.php?pass=" + pass_script + "&table=time&v1=" + str(data[15]).replace(" ", "%20"))
            u.close()
            lastTime = data[15]
            print data

while True:
    submitData()
    time.sleep(60)
    
    
    
