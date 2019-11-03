import weather, aligner, nexstar
import configparser, time

config = configparser.ConfigParser()

try:
    config.read('config.ini')
    targetName = config.get('target', 'name')
    targetMin = config.get('target', 'minHeight')
    targetRA = config.get('target', 'ra')
    targetDEC = config.get('target', 'dec')
except:
    print("Currupt config file!")
    print("Basic target information missing")
    print("Variable names may have been tampered with")
    quit()


if not nexstar.isConnected():
    #nexstar.connect()
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

print("")
print("Target:\t" + targetName)

while True:
    #try:
    while not weather.weatherStatus():
        print("Waiting for better weather conditions...")
        nexstar.setTrackingMode(0)
        pos = (round(nexstar.getAltAzi()[0]), round(nexstar.getAltAzi()[1]))
        if not pos == (-90,90):
            nexstar.gotoAltAzi(-90,90)
            print(pos)
        time.sleep(20)
            
    '''except:
        print("May not be connected to internet...")
        nexstar.setTrackingMode(0)
        nexstar.gotoAltAzi(0,0)
        time.sleep(600)'''
    
    
        
    


    
