from django.conf import settings
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from gmap.utils import geolocate
from gmap.models import MapMarker, MarkerCategory

import csv
import tempfile
import time

import gmap.utils

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

def dump_csv(request):

    all_markers = MapMarker.objects.all()

    print '# markers: ', len(all_markers)

    # all_markers should now have all the things...
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=map_markers.csv'

    #writer = csv.writer(response, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer = gmap.utils.UnicodeWriter(response, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    for marker in all_markers:
        row = marker.csv_row()
        #print 'row is: ', row

        # repr because there are non-ascii characters somewhere
        writer.writerow(row)

        '''
        writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        '''

    return response

def read_csv(request):

    if request.method == 'POST' and request.FILES.has_key('datafile'):

        # it's conceivable the user could upload a file large enough
        # it gets split into chunks - to handle this we just direct all
        # the chunks to a temp file and process that

        # note that the tempfile will be deleted as soon as
        # the with block is completes
        num_processed = -1
        delta = 0
                    
        errors = []
        if request.FILES['datafile'].multiple_chunks():

            delta = time.clock()

            with tempfile.TemporaryFile() as local_file:
        
                for chunk in request.FILES['datafile'].chunks():
                    local_file.write(chunk)

                local_file.seek(0)

                for row_id, row in enumerate(gmap.utils.UnicodeReader(local_file)):

                    marker = ''

                    try:
                        marker = MapMarker.objects.get(name=row[0])

                    except:
                        marker = MapMarker()

                    try:
                        marker.from_csv(row, row_id + 1, errors)

                    except Exception as inst:
                        errors.append("%s : Unable to import entry - %s" % (row_id, inst))

                    num_processed = row_id

            delta = time.clock() - delta

        else:

            delta = time.clock()

            for row_id, row in enumerate(gmap.utils.UnicodeReader(request.FILES['datafile'])):

                marker = ''

                try:
                    marker = MapMarker.objects.get(name=row[0])

                except:
                    marker = MapMarker()
                    
                try:
	                marker.from_csv(row, row_id + 1, errors)

                except Exception as inst:
                    errors.append("%s : Unable to import entry - %s" % (row_id, inst))

                num_processed = row_id

            delta = time.clock() - delta

        if len(errors) > 1:
            # Strip off errors result from Excel export garbage (the bottom two entries)
            #
            bottoms = errors[-2:]
            rows = [row.split(':')[0].strip() for row in bottoms]

            if int(rows[0]) == row_id:
                errors = errors[0:-2]

        if errors:
            return render_to_response('gmap_import_errors.html', {'errors' : errors})

        else:
            return HttpResponseRedirect('/admin/gmap/mapmarker/')

    else:
        # todo - can I make django redirect to referring page?
        return HttpResponseRedirect('/admin/gmap/')
        
