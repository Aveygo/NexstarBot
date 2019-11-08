import time, os

def takePhoto(shutter, iso, delay):
    try:
        os.system("gphoto2 --set-config shutterspeed=bulb")
        os.system("gphoto2 --set-config=/main/imgsettings/iso=" + str(iso))
	    os.sysytem('gphoto2 --set-config eosremoterelease=Immediate --wait-event=' + str(shutter) + 's --set-config eosremoterelease="Release Full"')
	    time.sleep(delay)
        return True
    except:
        return False