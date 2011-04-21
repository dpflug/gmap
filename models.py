from django.db import models
from gmap.utils import geolocate


class MarkerType(models.Model):
    category_name = models.CharField("type", max_length=200, unique=True)

    def __unicode__(self):
        return self.category_name


class MapMarker(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    marker_type = models.ForeignKey(MarkerType, "category_name")
    airport_code = models.CharField(max_length=6, blank=True)
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=40, blank=True)
    fax = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)

    # Make sure we update the lat/long with the location
    def save(self, *args, **kwargs):
        latlng = geolocate(self.address)
        self.latitude = latlng['latitude']
        self.longitude = latlng['longitude']
        super(MapMarker, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
