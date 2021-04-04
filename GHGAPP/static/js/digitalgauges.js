$(document).ready(function(){

	var speedGauge = new RadialGauge({
        renderTo: 'speedGauge',
        units: "KM/h",
        title: "Speed",
        minValue: 0,
        maxValue: 220,
        majorTicks: [
            0,20,40,60,80,100,120,140,160,180,200,220
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
        animationDuration: 500,
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

    var rpmGauge = new RadialGauge({
        renderTo: 'rpmGaugeCanva',
        units: "x 1000 RPM",
        minValue: 0,
        maxValue: 8000,
        majorTicks: [
            "0",
            "1000",
            "2000",
            "3000",
            "4000",
            "5000",
            "6000",
            "7000",
            "8000"
        ],
        minorTicks: 2,
        strokeTicks: true,
        highlights: [
            {
                "from": 6000,
                "to": 8000,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        borderShadowWidth: 0,
        borders: false,
        needleType: "arrow",
        needleWidth: 2,
        needleCircleSize: 7,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 500,
        animationRule: "linear",
        value: 120
    });

    var accelGauge = new RadialGauge({
        renderTo: 'accelGauge',
        units: "KM/h",
        title: "Acceleration",
        minValue: 0,
        maxValue: 220,
        majorTicks: [
            0,20,40,60,80,100,120,140,160,180,200,220
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
        animationDuration: 500,
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

    var fuelGauge = new RadialGauge({
        renderTo: 'fuelGauge',
        units: "l / KM",
        minValue: 0,
        maxValue: 8,
        majorTicks: [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        ],
        minorTicks: 2,
        strokeTicks: true,
        highlights: [
            {
                "from": 6,
                "to": 8,
                "color": "rgba(200, 50, 50, .75)"
            }
        ],
        colorPlate: "#fff",
        borderShadowWidth: 0,
        borders: false,
        needleType: "arrow",
        needleWidth: 2,
        needleCircleSize: 7,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 500,
        animationRule: "linear",
        value: 120
    });

    speedGauge.draw();
    rpmGauge.draw();
    accelGauge.draw();
    fuelGauge.draw();

    function updateReadings(){
        $.ajax({
            url: '/get_obd_real_data_gauges',
            success: function(response) {
                console.log(response);
                speedGauge.value = parseFloat(response['010D: Vehicle Speed'].replace(" kph",""));
                rpmGauge.value = parseFloat(response['010C: Engine RPM'].replace(" revolutions_per_minute",""));
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

	// every few seconds update reading values
    updateReadings();
    
	setInterval(function() {
        updateReadings();
	}, 1000);
});

$(window).on('resize', function(){
    resizeCanvas();
});

function resizeCanvas(){
    var canvasSpeed = $('#speedGauge');
    canvasSpeed.css("width", '100%');
    canvasSpeed.css("height", '100%'); 

    var canvasFuel = $('#fuelGauge');
    canvasFuel.css("width", '100%');
    canvasFuel.css("height", '100%'); 

    var canvasRPM = $('#rpmGaugeCanva');
    canvasRPM.css("width", '100%');
    canvasRPM.css("height", '100%'); 

    var canvasAccel = $('#accelGauge');
    canvasAccel.css("width", '100%');
    canvasAccel.css("height", '100%'); 

    var canvasGpsSpeed = $('#gpsSpeedGauge');
    canvasGpsSpeed.css("width", '100%');
    canvasGpsSpeed.css("height", '100%'); 
    
}
