from django.conf import settings
from django.shortcuts import render
from gmap.utils import geolocate
from gmap.models import MapMarker, MarkerType


def showmap(request, address='', category=''):
    context = {}
    context['media_url'] = settings.MEDIA_URL

    if request.method == 'POST':
        address = request.POST.get('address', address)
        category = request.POST.get('category', category)
    if request.method == 'GET':
        address = request.GET.get('address', address)
        category = request.GET.get('category', category)

    if category:
        context['gmap_markers'] = MapMarker.objects.get(marker_type__category_name__iexact=category)
    else:
        context['gmap_markers'] = MapMarker.objects.all()

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
