import json
import urllib
import urllib2


def geolocate(location, sensor=False):
    """
    Take a "location" and return its latitude and longitude

    Keyword arguments:
    location - String defining a geographical location (address, zip code, etc)
    sensor - Boolean defining whether the location was taken from
        an on-device sensor

    Output:
    latitude and logitude in an dict
    """
    sensor = str(sensor).lower()
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += urllib.urlencode({'address': location, 'sensor': sensor})
    data = urllib2.urlopen(url).read()
    data = json.loads(data)
    if data['status'] == 'OK':
        return({
               'latitude': data['results'][0]['geometry']['location']['lat'],
               'longitude': data['results'][0]['geometry']['location']['lng']
               })
