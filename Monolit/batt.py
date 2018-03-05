import smbus
import time

bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	return number

def readRaw():
	writeNumber(1)
	A0_1 = readNumber()
	
	writeNumber(2)
	A0_2 = readNumber()
	
	writeNumber(3)
	A1_1 = readNumber()
	
	writeNumber(4)
	A1_2 = readNumber()
	
	A0 = (A0_1 << 2) | A0_2
	A1 = (A1_1 << 2) | A1_2
	
	C0 = 1.0716 #correction values
	C1 = 0.9878

	V0 = A0*4.2/1023 * C0
	V1 = (A1*8.4/1023)* C1 

	return (V0, V1)

def readData():
	V0_sum = 0
	V1_sum = 0
	for i in range(5):
		(V0, V1) = readRaw()
		V0_sum += V0
		V1_sum += V1
	V0_sum /= 5
	V1_sum /= 5
	return (round(V0_sum, 2), round(V1_sum, 2))