from django.shortcuts import render
from gmap.models import MapMarker

def showmap(request, zipcode):
    context = {}
    if zipcode:
        context['zipcode'] = zipcode
    context['map_markers'] = MapMarker.objects.all()

    return render(request, 'map.html', context)
