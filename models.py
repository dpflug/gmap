import json
import urllib
import urllib2
from django.db import models


class MarkerType(models.Model):
    category_name = models.CharField("type", max_length=200, unique=True)

    def __unicode__(self):
        return self.category_name


class MapMarker(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField(max_length=200)
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    marker_type = models.ForeignKey(MarkerType, "category_name")

    # Make sure we update the lat/long with the location
    def save(self, *args, **kwargs):
        url = "http://maps.googleapis.com/maps/api/geocode/json?"
        url += urllib.urlencode({'address': self.location, 'sensor': 'false'})
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        self.latitude = data['results'][0]['geometry']['location']['lat']
        self.longitude = data['results'][0]['geometry']['location']['lng']
        print(self.latitude, self.longitude)
        super(MapMarker, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
