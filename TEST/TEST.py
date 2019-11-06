
import configparser, time, urllib
import datetime, math
config = configparser.ConfigParser()

try:
    config.read('config.ini')
    commandsFilepath = config.get('instructions', 'filepath')
    f = open(commandsFilepath, "r")
except:
    print("Could not open instruction file!")
    print("Make sure settings are correct inside config.ini")
    quit()


def readCommands():
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
            print(detail)

        elif instruction == "WAIT":
            time.sleep(int(detail))

        elif instruction == "PHOTO":
            for i in range(0, int(detail)):
                takePhoto()
                print("Took photo!")

        elif instruction == "TIME":
            detail = commands[i].split("TIME")[1][1:]
            #print(detail)

            daily = detail.split(" ")[0]
            #print(daily)
            year = daily.split(':')[0]
            month = daily.split(':')[1]
            day = daily.split(':')[2]

            hourly = detail.split(" ")[1]
            hour = hourly.split(':')[0]
            minute = hourly.split(':')[1]

            secondsToWait = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)) - datetime.datetime.now()
            secondsToWait = math.floor(secondsToWait.total_seconds())

            if secondsToWait < 0:
                secondsToWait = 0
                
            print(secondsToWait)

def takePhoto():
    var = False

readCommands()