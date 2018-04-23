from geoip import geolite2
from urllib.request import urlopen
import json

def get_location():
    maps_url=
    cont=urlopen(maps_url).read()
    components=data['results'][0]['formated_adress']
    return components

def main():
    ip=input('enter ip')
    match=geolite2.lookup(ip)

if __name__ == "__main__"
    main()