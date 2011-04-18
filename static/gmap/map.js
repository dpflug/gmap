var myLatlng = new Array();

myLatlng[0] = new google.maps.LatLng(28.5000, -81.4500);
var myOptions = {
    zoom: 10,
    center: myLatlng[0],
    mapTypeId: google.maps.MapTypeId.ROADMAP
}
var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

var marker = new Array();
var marker_content = new Array();
var marker_window = new Array();
marker[0] = new google.maps.Marker({
    position: myLatlng[0],
    map: map,
    title: "Hello world! " + "0"
});
marker_content[0] = 'This is a test window.'
marker_window[0] = new google.maps.InfoWindow({
    content: marker_content[0]
});
google.maps.event.addListener(marker[0], 'click', function() {
    marker_window[0].open(map, marker[0]);
});
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
    marker_window[{{ forloop.counter }}].open(map, marker[{{ forloop.counter }}]);
});
{% endfor %}
{% endautoescape %}
