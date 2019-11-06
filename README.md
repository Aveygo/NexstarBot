# NexstarBot
Currently this bot is in it's early stages and is fairly unusable. If needed, within the libraries folder, there are some scripts 
that might help your project such as serial commands and weather detection.

The aim is to make a python script that will read and run commands from an instruction file to control a Nexstar 
series telescope and a gphoto2 compatable camera. It will also be able to detect weather conditions and if they are too poor, 
will currently slew the telescope down and set it in hibernation mode.

The instruction file should be written with the following stucture:

The file must begin and end as such
BEGIN
...
END

Commands are currently;
SAY <string>                                    Will print string
WAIT <seconds (integer)>                        Will wait some amount of time
TIME <year>:<month>:<day> <hour>:<minute>       Will wait till specified time
PHOTO <amount (integers)                        Take specified amount of photos
SLEW <target name (string)>                     Slews to RA DEC of target in config.ini file
