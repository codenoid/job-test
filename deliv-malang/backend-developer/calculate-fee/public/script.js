var map
$(document).ready(function() {
    
    var malang = {
        lat: -7.956899,
        lng: 112.638842
    }

    map = new GMaps({
        div: '#map',
        center: malang
    })

    mark1 = map.addMarker({
        lat: -7.951074,
        lng: 112.639604,
        title: 'Satu',
        draggable: true,
        infoWindow: {
            content: 'Asal'
        }
    });

    mark2 = map.addMarker({
        lat: -7.954963,
        lng: 112.633477,
        title: 'Dua',
        draggable: true,
        infoWindow: {
            content: 'Tujuan'
        }
    });

});

function calculate() {
    var price = $('.price').val()
    var date = new Date()
    var current_hour = date.getHours()
    var url = "/calculate?" + "h=" + current_hour +
        "&price=" + price +
        "&lat1=" + mark1.getPosition().lat() +
        "&lon1=" + mark1.getPosition().lng() +
        "&lat2=" + mark2.getPosition().lat() +
        "&lon2=" + mark2.getPosition().lng()
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: (result) => {
            $('b#distance').html(result.distance + "KM - COST : Rp." + result.cost + " - SHARE : Rp." + result.share)
        }
    });
}

$("a.button").click(function() {
    calculate()
})