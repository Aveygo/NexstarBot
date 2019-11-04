import weather, aligner, nexstar
import configparser, time, socket, ping

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

def testInternet():
    try:
        ping.verbose_ping('www.google.com', count=3)
        delay = ping.Ping('www.wikipedia.org', timeout=2000).do()
    except socket.error, e:

        time.sleep(600)

def pointDown():
    nexstar.setTrackingMode(0)
    pos = (round(nexstar.getAltAzi()[0]), round(nexstar.getAltAzi()[1]))
    #if not already pointing down, point down
    if not pos == (-90,90):                     #An error either on line 41 or 42 (may not return proper position)
        nexstar.gotoAltAzi(-90,90) 

while True:
    #test weather
    try:    
        #while the weather is not good enough, point telescope down and wait till next best moment
        while not weather.weatherStatus():
            print("Waiting for better weather conditions...")
            pointDown()
            time.sleep(600) 

    #If the weather cannot be sourced...
    except:
            try:
                #Test internet connection
                print("Testing internet connection...")
                pointDown()
                if testInternet():
                    print("Cannot connect to weather open map!")
                    print("The API key might be wrong...")
                else:
                    print("Device offline, please connect...")
            except:
                try:
                    print("Testing device connection...")
                    if nexstar.isConnected():
                        print("FATAL ERROR: I have no idea what happened")
                    else:
                        print("Device was found to not be connected!")
                        print("Connecting...")
                        try:
                            nexstar.connect()
                        except:
                            print("Cannot connect to telescope.")
                            print("FATAL ERROR: I have no idea what happened")
                    
                
        

        
    


    
