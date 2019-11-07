# Basic controls of Nexstar celestron series, time and location set is probably broken and change com port if needed.
# Is 

import serial, time, math
from datetime import datetime
import configparser 

config = configparser.ConfigParser()
config.read('config.ini')

global port
port = str(config.get('comport', 'port'))

def connect(port = port):
	try:
		ser = serial.Serial(port)
		ser.open()
		ser.isOpen()
	except:
		ser = serial.Serial(port)
		ser.close()
		ser.open()
		ser.isOpen()
		
def isConnected():
	try:
		ser = serial.Serial(port)
		command = ("K" + chr('x') + "\r")
		ser.write(command.encode())
		response = ser.read(2).decode("utf-8")
		if response=="x#":
			return True
		else: 
			return False
	except:
		return False

def setTrackingMode(mode=1):	#0=off 1=ALT/AZ 2=EQNorth 3=EQSouth
	ser = serial.Serial(port)
	command = ("T" + chr(mode))
	ser.write(command.encode())
	ser.read()

def getAltAzi():	#returns ALT/AZ
	ser = serial.Serial(port)
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

def gotoAltAzi(Alt, Azi):	# Decimal -90,90 0,360
	ser = serial.Serial(port)
	Alt = format(int(Alt/360*65536), '04X')
	Azi = format(int(Azi/360*65536), '04X')
	command = ("B" + str(Azi) + "," + str(Alt))
	ser.write(command.encode())
	ser.read(1)

def gotoRaDec(Ra, Dec):	# Decimal 
	ser = serial.Serial(port)
	Ra = format(int(Ra/360*65536), '04X')
	Dec = format(int(Dec/360*65536), '04X')
	command = ("R" + str(Ra) + "," + str(Dec))
	ser.write(command.encode())
	ser.read(1)

def azmPos(rate): 
	ser = serial.Serial(port)
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(16) + chr(6) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	ser.read()

def azmNeg(rate):
	ser = serial.Serial(port)
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(16) + chr(7) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	ser.read()

def altPos(rate):
	ser = serial.Serial(port)
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(17) + chr(6) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	ser.read()

def altNeg(rate):
	ser = serial.Serial(port)
	rate = rate * 3600
	rateHigh = int((rate/4) / 256)
	rateLow = int((rate/4) % 256)
	command = ('P' + chr(3) + chr(17) + chr(7) + chr(rateHigh) + chr(rateLow) + chr(0) + chr(0))
	ser.write(command.encode())
	ser.read()

def isGoto():
	ser = serial.Serial(port)
	command = ("L")
	ser.write(command.encode())
	if int(ser.read()):
		return True
	else:
		return False

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

def setLocationHere(): 
	ser = serial.Serial(port)
	latitude = float(config.get('location', 'lat'))
	longitude = float(config.get('location', 'long'))

	A = int(math.floor(abs(latitude)))
	B = round(abs(latitude)-A, 5)*60
	C = int(round(B % 1,5)*60)

	B = int(math.floor(B))
	
	if latitude > 0:
		D = 1
	else:
		D = 0

	E = int(math.floor(abs(longitude)))
	F = round(abs(longitude)-E, 5)*60
	G = int(round(F % 1,5)*60)

	F = int(math.floor(F))

	if longitude > 0:
		H = 1
	else:
		H = 0	
	
	command = ('W' + chr(A) + chr(B) + chr(C) + chr(D) + chr(E) + chr(F) + chr(G) + chr(H))
	ser.write(command.encode())
	
