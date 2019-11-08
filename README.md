# NexstarBot
A script for nexstar series telescopes to handle overnight pre-set tasks and that detects poor weather conditions to alert the user.

Runs on Python 3.6+.

## Dependancies

Python Libraries:
* Configparser 
* Urllib

External:
* Gphoto2

Camera in use must be compatatble with gphoto2. The full list can be found [here](http://www.gphoto.org/proj/libgphoto2/support.php).

## Customising and writing your first script
NexstarBot allows the user to write a script that it reads and performs overnight. The default script is to wait untill midnight, point to M42, and take 20 photos.

The full list of available commands are:

* SAY (text)
Prints the text on the terminal.

* WAIT (seconds)
Sets a delay for said amount of seconds.

* PHOTO (amount)
Takes said amount of photos with pre-configured settings.
  
* TIME (year):(month):(date) (hour):(minute)
Waits untill time has been reached to continue.

* SLEW TARGET(id)
Slews the telescope to the target, more on the id part next.

### Config.ini
Inside config.ini you will see the option to edit settings inside target, camera settings, location, comport, and the path to instructions.nsb

#### Adding targets
To add a target to allow the bot to know where you want to point the telescope, you will have to add it's ra and dec coodinates into the config.ini file. The target information must contain name, ra, and dec (in decimal form). The header must be TARGET combined with a numerical value (e.g TARGET1, TARGET2), and must increment from the previous target starting at 1. By default the config.ini file contains 5 targets that should help you understand how it should be set out.

#### Camera Settings
Camera settings can be changed under [camera settings]. Shutter is in seconds, iso must follow typical iso settings (100, 200, 400, 1600, 6400 etc...), and delay is the amount of seconds the camera has to reset itself and by default is 1. 

#### Location
To successfully predict the weather, the location (latitude logitude) must be set roughly where you are located in decimal form. Height is also necessary.

#### Comport
In order for the bot to communicate with the telescope, the com port of the device must be specified. On windows you can find this in device manager and in linux based system in /dev/. 

## Running
Once you have connected the telescope and camera to the computer running the bot, starting it is as simple as 
```
python main.py
```
on windows and 
```
python3 main.py
```
on linux

## TODOs
* Detect if the target is 'sliding' away and to automatically readjust
* Automatically detect the serial port so the user does not have to type it in manually







