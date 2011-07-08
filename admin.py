from django.contrib import admin
from gmap.models import MapMarker, MarkerCategory, MarkerSubCategory


class MarkerAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'category',
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


admin.site.register(MapMarker, MarkerAdmin)
admin.site.register(MarkerCategory)
admin.site.register(MarkerSubCategory)
