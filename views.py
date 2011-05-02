from django.conf import settings
from django.shortcuts import render
from gmap.utils import geolocate
from gmap.models import MapMarker, MarkerType


def showmap(request, address=''):
    context = {}
    context['gmap_markers'] = MapMarker.objects.all()
    context['media_url'] = settings.MEDIA_URL

    if request.method == 'GET':
        address = request.GET.get('address', address)

    if address:
        latlng = geolocate(address)
        if latlng:
            context['gmap_center_lat'] = latlng['latitude']
            context['gmap_center_lng'] = latlng['longitude']
        else:
            context['error'] = "Please try another address."

    return render(request, 'gmap.html', context)


def markers(request):
    context = {}
    context['gmap_markers'] = MapMarker.objects.all()

    return render(request, 'gmap.js', context)


def gmap_search(request):
    context = {}
    return render(request, 'gmap_search.html', context)
