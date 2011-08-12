from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from gmap.utils import geolocate
from gmap.models import MapMarker, MarkerCategory

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
        context['gmap_markers'] = MapMarker.objects.get(
                marker_type__category_name__iexact=category
                )
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
    data = serializers.serialize("json", MapMarker.objects.all(),use_natural_keys=True)
    return HttpResponse(data, mimetype='applicaton/javascript')
    
def categories(request):
    data = serializers.serialize("json", MarkerCategory.objects.all().order_by('position'),use_natural_keys=True)
    return HttpResponse(data, mimetype='applicaton/javascript')

def gmap_search(request):
    context = {}
    return render(request, 'gmap_search.html', context)
