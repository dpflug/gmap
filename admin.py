from django.contrib import admin
from gmap.models import MapMarker, MarkerType


class MarkerAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'marker_type',
            'airport_code',
            'address',
            'phone',
            'fax',
            'email',
            'url'
           ]
    exclude = ('latitude', 'longitude')


class MarkerInline(admin.TabularInline):
    model = MapMarker
    exclude = ('latitude', 'longitude')
    extra = 1


class MarkerTypeAdmin(admin.ModelAdmin):
    inlines = [MarkerInline,]

admin.site.register(MapMarker, MarkerAdmin)
admin.site.register(MarkerType, MarkerTypeAdmin)
