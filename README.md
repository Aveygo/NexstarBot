# NexstarBot
A bot that can automatically handle current weather conditions, an easy to write script to direct the telescope without needing to wake up in the middle of the night, and libraries to move into your current projects if nessesary.
Runs on Python3.6+.
## Dependancies
* Configparser
* Urllib

## Customising
NexstarBot requires the user to instuct on what it must do inside commands.nsb and also requires configuration details inside config.ini
### Config.ini
Inside config.ini you will see targets, cammera settings, location, comport, and the path to instructions.nsb

#### Adding targets

[TARGET + #] 

name = Example

ra = -12.345

dec = 67.8901


## Running
As simple as
'''
python main.py
'''
