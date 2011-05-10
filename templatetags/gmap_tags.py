import re
from django import template
from gmap.models import MarkerType, MapMarker

register = template.Library()


class GmapMarkers(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = MapMarker.objects.all()


class GmapMarkerType(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = MarkerType.objects.all()
        return ''

def marker_types_tag(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
        print(token.contents.split(None, 1))
    except ValueError:
        raise template.TemplateSyntaxError(
                "%r tag requires arguments" % token.contents.split()[0])
    var_name = re.search(r'as (\w+)', arg).groups()[0]
    if not var_name:
        raise template.TemplateSyntaxError("%r tag had invalid arguments")
    return GmapMarkerType(var_name)


def markers_tag(parser, token):
    try:
        tag_name, arg = token.contents.split(None,1)
    except ValueError:
        raise template.TemplateSyntaxError(
                "%r tag requires arguments" % token.contents.split()[0])
    var_name = re.search(r'as (\w+)', arg).groups()[0]
    if not var_name:
        raise template.TemplateSyntaxError("%r tag had invalid arguments")
    return GmapMarkers(var_name)

register.tag('gmap_marker_types', marker_types_tag)
register.tag('gmap_markers', markers_tag)
