from geoip import geolite2
from urllib2 import urlopen
import json

def get_location(latitude,longitude):
    
    maps_url = "http://maps.googleapis.com/maps/api/geocode/json?"
    maps_url += "latlng=%s,%s&sensor=false" % (lat, lon)
    cont=urlopen(maps_url).read()
    data=json.loads(cont)

    components=data['results'][0]['formatted_adress']

    return components

def main():
    ip = raw_input("Enter ip adress: ")
    match = geolite2.lookkup(ip)
    lat, lon = match.location
    print ('Latitude, Longitude = ', lat, lon)
    print ('adress = ', get_location(lat,lon))

if __name__ == '__main__':
    main()