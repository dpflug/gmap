from django.db import models
from gmap.utils import geolocate

class MarkerCategoryManager(models.Manager):
    def get_by_natural_key(self,name):
        return self.get(name=name)

class MarkerCategory(models.Model):
    objects = MarkerCategoryManager()
    name = models.CharField('type', max_length=200, unique=True)
    icon = models.ImageField('icon', blank=True, upload_to='gmap-icons/')
    shadow = models.ImageField('icon shadow', blank=True, upload_to='gmap-icons/')
    def natural_key(self):
        return self.name  
    def __unicode__(self):
        return self.name

class MarkerSubCategory(models.Model):
    objects = MarkerCategoryManager()
    name = models.CharField('Name', max_length=200, unique=True)
    def natural_key(self):
        return self.name    
    def __unicode__(self):
        return self.name

class MapMarker(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey('MarkerCategory')
    sub_categories = models.ManyToManyField(MarkerSubCategory,related_name='sub_categories')
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
