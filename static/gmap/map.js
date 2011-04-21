var myLatlng = new Array();
var open_marker = '';

myLatlng[0] = new google.maps.LatLng(28.5000, -81.4500);

var myOptions = {
    zoom: 1,
    center: myLatlng[0],
    mapTypeId: google.maps.MapTypeId.ROADMAP
}
var map = new google.maps.Map(document.getElementById("gmap_canvas"), myOptions);

var marker = new Array();
var marker_content = new Array();
var marker_window = new Array();
{% autoescape on %}
{% for marker in map_markers %}
myLatlng[{{ forloop.counter }}] = new google.maps.LatLng({{ marker.latitude }}, {{ marker.longitude }});
marker[{{ forloop.counter }}] = new google.maps.Marker({
    position: myLatlng[{{ forloop.counter }}],
    map: map,
    title: "{{ marker.name|addslashes }}"
});
marker_content[{{ forloop.counter }}] = '<p>Title: {{ marker.name|escapejs }}</p>' +
    '<p>Airport code: {{ marker.airport_code|escapejs }}</p>' +
    '<p>Address: <pre>{{ marker.address|escapejs }}</pre></p>' +
    '<p>Phone: {{ marker.phone|escapejs }}</p>' +
    '<p>Fax: {{ marker.fax|escapejs }}</p>' +
    '<p>Email: {{ marker.email|escapejs }}</p>' +
    '<p><a href="{{ marker.url|escapejs }}">Visit their website</a></p>';
marker_window[{{ forloop.counter }}] = new google.maps.InfoWindow({
    content: marker_content[{{ forloop.counter }}]
});
google.maps.event.addListener(marker[{{ forloop.counter }}], 'click', function() {
    if (open_marker != '') {
        open_marker.close();
    }
    open_marker = marker_window[{{ forloop.counter }}];
    marker_window[{{ forloop.counter }}].open(map, marker[{{ forloop.counter }}]);
});
{% endfor %}
{% endautoescape %}
