function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 40.7128, lng: -74.0060 },
        zoom: 4
    });

    var optimizedRoute = {{ optimized_route | tojson }};
    var routeCoordinates = [];

    for (var i = 0; i < optimizedRoute.length - 1; i++) {
        var station1 = optimizedRoute[i];
        var station2 = optimizedRoute[i + 1];
        // Add coordinates for each station
        routeCoordinates.push(new google.maps.LatLng(station1.lat, station1.lng));
        routeCoordinates.push(new google.maps.LatLng(station2.lat, station2.lng));
    }

    var route = new google.maps.Polyline({
        path: routeCoordinates,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
    });

    route.setMap(map);
}
