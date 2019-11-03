from astropy.coordinates import EarthLocation,SkyCoord
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz

def convert(longi, lati, height, time,):

    observing_location = EarthLocation(lat='52.2532', lon='351.63910339111703', height=100*u.m)  
    observing_time = Time('2017-02-05 20:12:18')  
    aa = AltAz(location=observing_location, obstime=observing_time)

    coord = SkyCoord('4h42m', '-38d6m50.8s')
    coord.transform_to(aa)