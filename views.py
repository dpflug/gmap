from django.shortcuts import render
from gmap.models import MapMarker


def showmap(request, zipcode):
    context = {}
    if zipcode:
        context['zipcode'] = zipcode
        # TODO: Geolocate their zip and pass that lat/lng to set the map bounds
    context['map_markers'] = MapMarker.objects.all()

    return render(request, 'map.html', context)


def markers(request):
    context = {}
    context['map_markers'] = MapMarker.objects.all()

    return render(request, 'map.js', context)
