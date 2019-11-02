import weather
import configparser 

config = configparser.ConfigParser()

config.read('config.ini')

test = config.get('DF settings', 'shutter')
print(test)
