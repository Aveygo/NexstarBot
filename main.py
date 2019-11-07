from libraries import weather, aligner, nexstar
import configparser, time, urllib, datetime

config = configparser.ConfigParser()

targetlist = []

try:
    config.read('config.ini')    
    targetName = config.get('TARGET1', 'name')
    targetRA = config.get('TARGET1', 'ra')
    targetDEC = config.get('TARGET1', 'dec')
    targetlist.append([targetName, targetRA, targetDEC])
except:
    print("Currupt config file!")
    print("Basic target information missing")
    print("Variable names may have been tampered with")
    quit()

for i in range(2, 100):
    try:
        targetID = "TARGET" + str(i)
        targetName = config.get(targetID, 'name')
        targetRA = config.get(targetID, 'ra')
        targetDEC = config.get(targetID, 'dec')
        targetlist.append([targetName, targetRA, targetDEC])
    except:
        break

print("")
print("Following targets detected:")
for i in range(0, len(targetlist)):
    print("\t " + targetlist[i][0])
print("")

try:
    cameraShutter = config.get('camera settings', 'shutter')
    cameraISO = config.get('camera settings', 'iso')
    cameraDelay = config.get('camera settings', 'delay')
except:
    print("Currupt config file!")
    print("Basic camera settings missing")
    print("Variable names may have been tampered with")
    quit()

try:
    commandsFilepath = config.get('instructions', 'filepath')
    f = open(commandsFilepath, "r")
except:
    print("Could not open instruction file!")
    print("Make sure settings are correct inside config.ini")
    quit()


if not nexstar.isConnected():
    print("Connecting to telescope")
    print("")
    try:
        nexstar.connect()
    except:
        try:
            nexstar.connect()
        except:
            print("Failed to connect to telescope!")
            print("Try changing default COM port in config.ini")
            quit()
else:
    print("Connection made with telecope...")


def testInternet():
    try:
        stri = "https://www.google.com"
        urllib.urlopen(stri)
        return True
    except:
        return False

def pointDown():
    nexstar.setTrackingMode(0)
    pos = (round(nexstar.getAltAzi()[0]), round(nexstar.getAltAzi()[1]))
    #if not already pointing down, point down
    if not pos == (-90,90):                     #An error either on line 41 or 42 (may not return proper position)
        nexstar.gotoAltAzi(-90,90) 

def debug():
    try:
        print("Testing internet connection...")
        if testInternet():
            print("Cannot connect to weather open map!")
            print("The API key might be wrong...")
        else:
            print("Device offline, please connect...")
    except:
        print("Testing device connection...")
        if nexstar.isConnected():
            print("FATAL ERROR: I have no idea what happened")
        else:
            print("Device was found to not be connected!")
            print("Connecting...")
            try:
                nexstar.connect()
            except:
                print("Telescope refuses to connect...")
                print("FATAL ERROR: I have no idea why this happened")


def genCommands():
    commandsClean = []
    try:
        commands = []
        line = f.readline()
        while not line == "END":
            commands.append(line)
            line = f.readline()

        commands.append(line)

        for i in range(0, len(commands)):
            commands[i] = commands[i].rstrip("\n")
            
        commands = commands[1:-1]

        for i in range(0, len(commands)):
            instruction = commands[i].split(" ")[0]
            detail = commands[i].split(" ")[1]

            if instruction == "SAY":
                detail = commands[i].split("SAY")[1][1:]
                commandsClean.append([instruction, detail])

            elif instruction == "WAIT":
                commandsClean.append([instruction, int(detail)])

            elif instruction == "PHOTO":
                for i in range(0, int(detail)):
                    commandsClean.append([instruction, int(detail)])

            elif instruction == "SLEW":
                commandsClean.append([instruction, detail])

            elif instruction == "TIME":
                detail = commands[i].split("TIME")[1][1:]

                daily = detail.split(" ")[0]

                year = daily.split(':')[0]
                month = daily.split(':')[1]
                day = daily.split(':')[2]

                hourly = detail.split(" ")[1]
                hour = hourly.split(':')[0]
                minute = hourly.split(':')[1]

                specificTime = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
                commandsClean.append([instruction, specificTime])
    except:
        return False

    return commandsClean 

################################ START CODE ########################################

global weatherStatus

commands = genCommands()
if commands == False:
    print("Error while commands were read, please check for errors!")
    quit()

currentCommandLine = 0

def runningWeatherDetection():
    while True:
        try:    
            while not weather.weatherStatus():
                print("Waiting for better weather conditions...")
                weatherStatus = False
                pointDown()
                time.sleep(600) 
            weatherStatus = True    
        except:
            pointDown()
            weatherStatus = False
            debug()


def runningTelescopeBot():    
    while weatherStatus:
        action = commands.curentCommandLine[0]
        info = commands.curentCommandLine[1]

        if action == "SAY":
            print(info)

        if action == "WAIT":
            time.sleep(info)
        
        if action == "PHOTO":
            camcontrol.takephoto(cameraShutter, cameraISO, cameraDelay)
            time.sleep(cameraShutter + cameraDelay)

        if action == "SLEW":
            targetNum = detail.replace("TARGET", "")
            ra = targetlist[targetNum][1]
            dec = targetlist[targetNum][2]
            nexstar.gotoRaDec(ra, dec)

            while nexstar.isGoto():
                time.sleep(1)








