# Basic controls of Nexstar celestron series, time and location set is probably broken and change com port if needed.
# Is 

timezone = -10 #From UTC
# TODO - location

import serial, time, keyboard
from datetime import datetime

ser = serial.Serial("COM3")
ser.open()
ser.isOpen()

def getPos():	#returns ALT/AZ
	command = ("Z\r")
	ser.write(command.encode())
	response = ser.read(10).decode("utf-8")
	data = response.split(",")
	azi = data[0]
	alt = data[1]
	alt = alt[:4]
	azi = int(azi, 16)/65536*360
	alt = int(alt, 16)/65536*360
	return alt, azi

def gotoAltAzi(Alt, Azi):	# Decimal
	Alt = format(int(Alt/360*65536), '04X')
	Azi = format(int(Azi/360*65536), '04X')
	command = ("B" + str(Azi) + "," + str(Alt))
	ser.write(command.encode())
	response = ser.read(1)

def gotoRaDec(Ra, Dec):	# Decimal
	Ra = format(int(Ra/360*65536), '04X')
	Dec = format(int(Dec/360*65536), '04X')
	command = ("R" + str(Ra) + "," + str(Dec))
	ser.write(command.encode())
	response = ser.read(1)

def azmPos(rate): # In the 0.0.1 update, Needs to convert degrees to arc seconds
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(16) + chr(6) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	response = ser.read()

def azmNeg(rate):
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(16) + chr(7) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	response = ser.read()

def altPos(rate):
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(17) + chr(6) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	response = ser.read()

def altNeg(rate):
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(17) + chr(7) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	response = ser.read()

'''	#Broken!!!
def setTimeNow(): 
    V = datetime.now().year - 2000
    T = datetime.now().month
    U = datetime.now().day
    Q = datetime.now().hour
    R = datetime.now().minute
    S = datetime.now().second
    W = 256 + timezone
    X = 1	#0 standard, 1 daylight savings
    command = ('H' + chr(Q) + chr(R) + chr(S) + chr(T) + chr(U) + chr(V) + chr(W) + chr(X))
    ser.write(command.encode())
'''
def setLocationHere(): #151.13.19 S , -33.46.50 E
    A = 33
    B = 46
    C = 50
    D = 1
    E = 151
    F = 13
    G = 19
    H = 0
    command = ('W' + chr(A) + chr(B) + chr(C) + chr(D) + chr(E) + chr(F) + chr(G) + chr(H))
    ser.write(command.encode())
    



        



