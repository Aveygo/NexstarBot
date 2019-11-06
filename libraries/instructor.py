
import configparser, time, urllib
import datetime, math
import camcontrol
config = configparser.ConfigParser()

try:
    config.read('.././config.ini')
    commandsFilepath = config.get('instructions', 'filepath')
    f = open(commandsFilepath, "r")
except:
    print("Could not open instruction file!")
    print("Make sure settings are correct inside config.ini")
    quit()



