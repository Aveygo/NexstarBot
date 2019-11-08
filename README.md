# NexstarBot
A bot that can automatically handle current weather conditions, an easy to write script to direct the telescope without needing to wake up in the middle of the night, and libraries to move into your current projects if nessesary.
Runs on Python3.6+.
## Dependancies
* Configparser
* Urllib

## Customising
NexstarBot requires the user to instuct on tasks it must do inside commands.nsb and requires configuration details inside config.ini

### Config.ini
Inside config.ini you will see the option to edit settings inside target, cammera settings, location, comport, and the path to instructions.nsb

#### Adding targets
To add a target to allow the bot to know where you want to point the telescope, you will have to add it's ra and dec coodinates into the config.ini file. The target information must contain name, ra, and dec (in decimal form). The header must be TARGET combined with a numerical value (e.g TARGET1, TARGET2), and must increments from the previous one starting at 1. By default they're 5 targets that you can slew to to test if the system works and to provide an example on how it is organised.

#### Camera Settings
Currently NexstarBot cannot change camera settings while running, but settings can be changed under [camera settings]. Shutter is in seconds, iso must follow typical iso settings (100, 200, 400, 1600, 6400 etc...), and delay is the amount of seconds the camera has to reset itself and should be no less than 1. 

#### Location
To successfully predict the weather, the location must be set roughly where you are located in decimal form. Height is also necessary.

#### Comport
In order for the bot to communicate with the telescope, the com port of the device must be specified. On windows you can find this in device manager and on linux based system in /dev/.

## Running
