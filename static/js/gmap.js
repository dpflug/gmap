function toggleCategory(category) {
    var markers = window.markers
    for (marker in window.markers[category]) {
        if (typeof category_visible == 'undefined') {
            // Set a variable for the whole category so things don't get out of sorts if people get click-happy
            var category_visible = !(markers[category][marker]['visible']);
            markers[category][marker]['visible'] = category_visible;
        };
        markers[category][marker]['marker'].setVisible(category_visible);
    }
    return false;
}

$(document).ready(function() {

    var myLatlng = new Array();
    var open_marker = '';
    
    myLatlng[0] = new google.maps.LatLng(28.5000, -81.4500);
    
    var map = new google.maps.Map(document.getElementById("gmap_canvas"), {
        zoom: 1,
        center: myLatlng[0],
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
   
    var markers = []
    
    $.getJSON('/map/markers.json',function(data){
        var categories = new Array();
        var sub_categories = new Array();
        $.each(data, function(key,item){
            var latLng = new google.maps.LatLng(item.fields.latitude,item.fields.longitude)
            markers[item.fields.name] = {}
            markers[item.fields.name]['marker'] = new google.maps.Marker({
                position: latLng,
                map : map,
                title: item.fields.name
            })
            var content = '<span class="name">'+item.fields.name+'</span><br/><span class="phone">'+item.fields.phone+'</span><br/><span class="email">'+item.fields.email+'</span><br/><span class="url">'+item.fields.url+'</span><br/>'
            markers[item.fields.name]['window'] = new google.maps.InfoWindow({
                content: content
            });
            google.maps.event.addListener(
                markers[item.fields.name]['marker'], 'click', function(){
                    if (open_marker != '') {
                        open_marker.close();
                    }
                    open_marker = markers[item.fields.name]['window'];
                    open_marker.open(
                        map,
                        markers[item.fields.name]['marker']
                    );
                }
            );
            if ($.inArray(item.fields.category,categories) == -1){
                categories.push(item.fields.category)
                $('#gmap_categories').append('<a href="#category_'+item.fields.category+'">'+item.fields.category+'</a>')
            }
            $.each(item.fields.sub_categories,function(key,item){
                if ($.inArray(item,sub_categories) == -1){
                    sub_categories.push(item)
                    $('#gmap_sub_categories').append('<a href="#sub_category_'+item+'">'+item+'</a>')
                }
            })
            console.log(item)
        })
    })
 
    google.maps.event.addListener(map, 'click', function(){
        if (open_marker != '') {
            open_marker.close();
        }
        open_marker = '';
    });
    
})
