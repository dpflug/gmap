from django.contrib import admin
from gmap.models import MapMarker, MarkerCategory, MarkerSubCategory, SalesDirector, SalesBoundary


class MarkerAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'contact_title',
            'category',
            'contact_name',
            'airport_code',
            'address',
            'platinum',
            'airport_name',
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
    
class BoundaryAdmin(admin.ModelAdmin):
    list_display = ['boundary_code', 'owner']


admin.site.register(MapMarker, MarkerAdmin)
admin.site.register(MarkerCategory)
admin.site.register(MarkerSubCategory)
admin.site.register(SalesDirector)
admin.site.register(SalesBoundary, BoundaryAdmin)
