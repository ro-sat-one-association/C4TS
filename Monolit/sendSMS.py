import gsm as GSM

for i in range(0,3): #incearca de 3 ori sa-l pornesti
	if (GSM.isAlive() == False):
		GSM.StartStop()
	else:
		break