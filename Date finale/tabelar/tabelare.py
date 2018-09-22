#!/usr/bin/env python
# -*- coding: utf-8 -*-

date  = open("Date.txt")
tabel = open("tabel.txt", 'w+')

c = 0
printline = ""

data = ""
ora = ""
lat = ""
lon = "" 
altit = ""
t_bmp = ""
t_ds  = ""
t_ext = ""
pres  = ""
umid  = ""
tsl_ir  = ""
tsl_tot = ""
v_cel   = ""
v_tot   = ""

while True:
    s = date.readline()
    if s.find("2018-09") != -1:
        data= s.split(" ")[0]
        ora = s.split(" ")[1]
    
    if s.find("BMP") != -1:
        try:
            s = s.split("(")[1]
        except:
            s = s.split("[")[1]
            
        t_bmp = s.split(",")[0]
        pres += s.split(",")[1][:-2]
       
    if s.find("GPS") != -1:
        s = s.split("[")[1]
        lat = s.split(",")[0]
        lon = s.split(",")[1]
        altit = s.split(",")[2][:-2]
        altit = altit.replace("'", "")
        
        lat  = lat[:3][1:] + "°" + lat[:5][3:] + "'" + str(float(lat.split(".")[1].split("'")[0][:-1])*0.6) + "\"" + "N"
        lon  = lon[:5][3:] + "°" + lon[:7][5:] + "'" + str(float(lon.split(".")[1].split("'")[0][:-1])*0.6) + "\"" + "E"
        
    if s.find("DS18") != -1:
        t_ds = s.split(" ")[1][:-1]
    
    if s.find("TSL") != -1:
        tsl_tot = s.split("(")[1].split(",")[0]
        tsl_ir = s.split("(")[1].split(",")[1][:-2]
    
    if s.find("SHT") != -1:
        t_ext = s.split("(")[1].split(",")[0]
        umid  = s.split("(")[1].split(",")[1][:-2]
    
    if s.find("BAT") != -1:
        try:
            v_cel = s.split("(")[1].split(",")[0]
            v_tot  = s.split("(")[1].split(",")[1][:-2]
        except:
            v_cel = "-1"
            v_tot = "-1"

#Ora Poz Altit_GPS T_BMP T_DS T_ext Presiune Umiditate TSL_tot TSL_ir V_Total V_cel
            
    if s == "\n":
        printline = ""
        printline += data  + " " + ora[:-8] + " " + lat + " " + lon + " "
        printline += altit + " " + t_bmp + " " + t_ds + " " + t_ext + " "
        printline += pres  + " " + umid  + " " + tsl_tot + " " + tsl_ir + " "
        printline += v_tot + " " + v_cel + "\n"
        print printline
        tabel.write(printline)
        data = ""
        ora = ""
        lat = ""
        lon = "" 
        altit = ""
        t_bmp = ""
        t_ds  = ""
        t_ext = ""
        pres  = ""
        umid  = ""
        tsl_ir  = ""
        tsl_tot = ""
        v_cel   = ""
        v_tot   = ""
