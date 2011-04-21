var myLatlng = new Array();
var open_marker = '';

myLatlng[0] = new google.maps.LatLng(28.5000, -81.4500);

var map = new google.maps.Map(document.getElementById("gmap_canvas"), {
    zoom: 1,
    center: myLatlng[0],
    mapTypeId: google.maps.MapTypeId.ROADMAP
});

var markers = [];

google.maps.event.addListener(map, 'click', function(){
    if (open_marker != '') {
        open_marker.close();
    }
    open_marker = '';
});

{% for category in marker_types %}
markers['{{ category|escapejs }}'] = [];
{% endfor %}

{% for marker in map_markers %}
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}'] = [];
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['visible'] = true;
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['latlng'] =
    new google.maps.LatLng({{ marker.latitude }}, {{ marker.longitude }});
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['marker'] = new google.maps.Marker({
    position: markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['latlng'],
    map: map,
    title: "{{ marker|escapejs }}"
});
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['content'] =
    '<p>Title: {{ marker|escapejs }}</p>' +
    '<p>Airport code: {{ marker.airport_code|escapejs }}</p>' +
    '<p>Address: <pre>{{ marker.address|escapejs }}</pre></p>' +
    '<p>Phone: {{ marker.phone|escapejs }}</p>' +
    '<p>Fax: {{ marker.fax|escapejs }}</p>' +
    '<p>Email: {{ marker.email|escapejs }}</p>' +
    '<p><a href="{{ marker.url|escapejs }}">Visit their website</a></p>';
markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['window'] = new google.maps.InfoWindow({
    content: markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['content']
});
google.maps.event.addListener(
    markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['marker'],
    'click',
    function(){
        if (open_marker != '') {
            open_marker.close();
        }
        open_marker = markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['window'];
        markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['window'].open(
            map,
            markers['{{ marker.marker_type|escapejs }}']['{{ marker|escapejs }}']['marker']
        );
});

{% endfor %}

function toggleCategory(category) {
    for (marker in markers[category]) {
        if (typeof category_visible == 'undefined') {
            // Set a variable for the whole category so things don't get out of sorts if people get click-happy
            var category_visible = !(markers[category][marker]['visible']);
            markers[category][marker]['visible'] = category_visible;
        };
        markers[category][marker]['marker'].setVisible(category_visible);
    }
    return false;
}

