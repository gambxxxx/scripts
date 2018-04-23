from geoip import geolite2
from urllib.request import urlopen
import json

def get_location(lat_coords,long_coords):
    maps_url="http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=false" % (lat_coords,long_coords)
    cont=urlopen(maps_url).read()
    data=json(cont)
        
    components=data['results'][0]['formatted_adress']
    return components

def main():
    ip = input("Enter ip adress")
    match = geolite2.lookup(ip)
    lat,lon = match.location
    print("Lattitude, Longitude = ".format(lat,lon))
    print("address = ",get_location(lat,lon))

if __name__ == "__main__":
    main()