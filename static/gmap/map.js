var myLatlng = new Array();
{% if zip %}

myLatlng[0] = new google.maps.LatLng(28.5000, -81.4500);
var myOptions = {
    zoom: 9,
    center: myLatlng[0],
    mapTypeId: google.maps.MapTypeId.ROADMAP
}
var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

var marker = new Array();
marker[0] = new google.maps.Marker({
    position: myLatlng[0],
    map: map,
    title: "Hello world! " + "0"
});
{% autoescape on %}
{% for marker in map_markers %}
myLatlng[{{ forloop.counter }}] = new google.maps.LatLng({{ marker.latitude }}, {{ marker.longitude }});
marker[{{ forloop.counter }}] = new google.maps.Marker({
    position: myLatlng[{{ forloop.counter }}],
    map: map,
    title: "{{ marker.name|addslashes }}"
});
{% endfor %}
{% endautoescape %}
