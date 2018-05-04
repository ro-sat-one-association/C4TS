import sys
import time
import difflib
import pigpio
import subprocess

TX  = 27
RX  = 17
fisier = "/home/pi/Final/gsm.txt"

subprocess.call(["gpio", "mode", "1", "output"])
subprocess.call(["gpio", "write", "1", "1"])

def write(state):
    subprocess.call(["gpio", "write", "1", str(state)])

def Tx(data):
    try:
            pi = pigpio.pi()
            pi.set_mode(TX, pigpio.OUTPUT)
            pi.wave_clear()
            pi.wave_add_serial(TX, 9600, data)
            wid=pi.wave_create()
    
            pi.wave_send_once(wid)   # transmit serial data
            pi.wave_delete(wid)
    
    except:
            pi.stop()

def Rx(nr_linii = 1):
    f = open(fisier)
    linii = []
    linii = f.readlines()
    data = ""
    if len(linii) > nr_linii:
        for i in range(0, len(linii)):
            data += str(linii[len(linii)-1-i])
    else:
        for e in linii:
            data += str(e)
    return data

def startStop():
    write(0)
    time.sleep(2)
    write(1)
    
def isAlive():
    t = str(time.time())
    Tx(t + "\r")
    time.sleep(1)
    output = Rx(2)
    if (str(output).find(t) != -1):
        return True
    return False

def start():
    if not isAlive():
        startStop()
        
def stop():
    Tx("AT+CPWROFF\r")

def sendSMS(numar, sms):
    f = open(fisier, "w")
    f.close()
    stop()
    time.sleep(1)
    start()
    t = time.time()
    while (Rx(100).find("PBREADY") == -1):
        if time.time() - t > 15:
            print "NU AM GASIT PBREADY"
            break
        time.sleep(1)
    
    Tx("AT+CREG=1\r")
    time.sleep(1)
    Tx("AT+CSMS=1\r")
    time.sleep(1)
    Tx("AT+CMGF=1\r")	
    time.sleep(1)
    Tx("AT+CSCS=\"GSM\"\r")
    time.sleep(1)
    Tx("AT+CMGS=\"" + numar + "\"\r")
    time.sleep(2)
    Tx(sms)
    time.sleep(1)
    Tx("\r")
    t = time.time()
    while (Rx(4).find("+CMGS:") == -1):
        if time.time() - t > 10:
            stop()
            return False
        time.sleep(1)
    stop()
    return True
