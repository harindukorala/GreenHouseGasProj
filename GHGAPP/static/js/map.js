
$(document).ready(function () {

    setInterval(function() {
      updateMarkerPositions();
    }, 1000);
});

var marker;
var map;
var gpsSpeedGauge;

function initMap(){
  map = new google.maps.Map(document.getElementById('map'), {zoom: 12});
  marker = new google.maps.Marker();

  gpsSpeedGauge = new RadialGauge({
    renderTo: 'gpsSpeedGauge',
    units: "KM/h",
    title: "Speed",
    minValue: 0,
    maxValue: 220,
    majorTicks: [
        0,20, 40, 60 ,80,100, 120, 140, 160, 180, 200, 220
    ],
    minorTicks: 2,
    strokeTicks: true,
    highlights: [
        {
            "from": 0,
            "to": 160,
            "color": "rgba(0,0, 255, .3)"
        },
        {
            "from": 160,
            "to": 220,
            "color": "rgba(255, 0, 0, .3)"
        }
    ],
    ticksAngle: 225,
    startAngle: 67.5,
    colorMajorTicks: "#ddd",
    colorMinorTicks: "#ddd",
    colorTitle: "#eee",
    colorUnits: "#ccc",
    colorNumbers: "#eee",
    colorPlate: "#222",
    borderShadowWidth: 0,
    borders: true,
    needleType: "arrow",
    needleWidth: 2,
    needleCircleSize: 7,
    needleCircleOuter: true,
    needleCircleInner: false,
    animationDuration: 1500,
    animationRule: "linear",
    colorBorderOuter: "#333",
    colorBorderOuterEnd: "#111",
    colorBorderMiddle: "#222",
    colorBorderMiddleEnd: "#111",
    colorBorderInner: "#111",
    colorBorderInnerEnd: "#333",
    colorNeedleShadowDown: "#333",
    colorNeedleCircleOuter: "#333",
    colorNeedleCircleOuterEnd: "#111",
    colorNeedleCircleInner: "#111",
    colorNeedleCircleInnerEnd: "#222",
    valueBoxBorderRadius: 0,
    colorValueBoxRect: "#222",
    colorValueBoxRectEnd: "#333"
});

  gpsSpeedGauge.draw();

  updateMarkerPositions();
}

function updateMarkerPositions(){
  $.ajax({
      url: '/get_gps_data',
      success: function(response) {
          gpsSpeedGauge.value = response['Speed'];
          var LatLng = new google.maps.LatLng(response['Latitude Degree'], response['Longitude Degree']);
          marker.setPosition(LatLng);
          marker.setMap(map);
          map.setCenter(LatLng);
          //marker.setAnimation(google.maps.Animation.BOUNCE);
      },
      error: function(error) {
          console.log(error);
      }
  });
}





















