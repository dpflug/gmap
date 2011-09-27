from django import forms
from gmap.models import MapMarker

class ModifiedChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if 'country' in obj:
            return obj['country']

        if 'state' in obj:
            return obj['state']

        return 'No Data'

class MapSearchForm(forms.Form):
    state = ModifiedChoiceField(queryset=MapMarker.objects.filter(country='United States').values('state').distinct(), label='')
    country = ModifiedChoiceField(queryset=MapMarker.objects.values('country').distinct(), label='')
