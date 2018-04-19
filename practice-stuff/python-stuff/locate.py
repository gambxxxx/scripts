import urllib
from urllib import urlopen
import json
import re

# Get Public IP


def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details
print (f"Your City : " + city)
print (f"Your Region : " + region)
print (f"Your Country : " + country)
print (f"Your Location : " + location)