import weather, aligner, nexstarControls
import configparser 

config = configparser.ConfigParser()

config.read('config.ini')

targetName = config.get('target', 'name')
targetRA = config.get('target', 'ra')
targetDEC = config.get('target', 'dec')

