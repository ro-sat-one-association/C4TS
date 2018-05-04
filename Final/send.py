from collect import Data
from collect import APRSToSend
import aprs as APRS
import time

APRS1   = "="
APRS1  += Data["GPS"][0]
APRS1  += "/" #indicator tabel
APRS1  += Data["GPS"][1]
APRS1  += "_" #_ - wx O - balon
#APRS1  = "=4656.32N/02623.56E_" 
APRS1 += "c...s...g...t"


def CtoF(temp):
	return str(int(temp*1.8 + 32))

def getAPRSAltitude(altitude):
	altitude = int(float(altitude) * 3.28084)
	returnStr = ""
	for i in range(0, 6 - len(str(altitude))):
		returnStr += "0"
	returnStr += str(altitude)
	return returnStr
	
###TEMPERATURA BMP###
if int(CtoF(Data["BMP"][0])) >= 0:
	if int(CtoF(Data["BMP"][0])) < 100:
		APRS1 += "0"
		if int(CtoF(Data["BMP"][0])) < 10:
			APRS1 += "0"
	APRS1 += CtoF(Data["BMP"][0])	
else:
	if int(CtoF(Data["BMP"][0])) > -10:
		APRS1 += "-0"
		APRS1 += str(-int(CtoF(Data["BMP"][0])))
	else:
		APRS1 += CtoF(Data["BMP"][0])	
#####################


###UMIDITATE SHT###
APRS1 += "h"
APRS1 += str(int(Data["SHT"][1]))
###################


###PRESIUNE BMP###
APRS1 += "b" 
tailingZeros = 5 - len(str(int(Data["BMP"][1]*10)))
for i in range(tailingZeros):
	APRS1 += "0"	
if tailingZeros < 0:
	APRS1 += "....."
else:
	APRS1 += str(int(Data["BMP"][1]*10))
##################	

print APRS.send(APRS1)
print APRS1

time.sleep(3)

APRS2   = "="
APRS2  += Data["GPS"][0]
APRS2  += "/" #indicator tabel
APRS2  += Data["GPS"][1]
APRS2  += "O" #_ - wx O - balon 
APRS2  += APRSToSend
APRS2 += "/A="
APRS2 += getAPRSAltitude(Data["GPS"][2])

print APRS.send(APRS2)

print APRS2