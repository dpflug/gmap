from django.shortcuts import render
from gmap.utils import geolocate
from gmap.models import MapMarker, MarkerType


def showmap(request, address=''):
    context = {}
    context['map_markers'] = MapMarker.objects.all()

    if request.method == 'GET':
        address = request.GET.get('address', address)

    if address:
        latlng = geolocate(address)
        if latlng:
            context['map_center_lat'] = latlng['latitude']
            context['map_center_lng'] = latlng['longitude']
        else:
            context['error'] = "Please try another address."

    return render(request, 'map.html', context)


def markers(request):
    context = {}
    context['map_markers'] = MapMarker.objects.all()

    return render(request, 'map.js', context)


def gmap_search(request):
    context = {}
    return render(request, 'map_search.html', context)
