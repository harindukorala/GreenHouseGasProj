var chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

var color = Chart.helpers.color;

var config = {
	type: 'line',
	data: {
		datasets: [{
			label: 'CO2 %',
			backgroundColor: color(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: false,
			lineTension: 0,
			borderDash: [8, 4],
			data: [{x: Date.parse('2020-11-02 18:30:23.345330'), y:0}]
		}, {
			label: 'CO %',
			backgroundColor: color(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: false,
			data: [{x: Date.parse('2020-11-02 18:30:23.345330'), y:0}]
    },
    {
			label: 'O2 %',
			backgroundColor: color(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			fill: false,
			data: [{x: Date.parse('2020-11-02 18:30:23.345330'), y:0}]
		}]
	},
	options: {
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: 20000,
					refresh: 5000,
					delay: 2000,
					onRefresh: getLiveGasData
				}
			}],
			yAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'value'
				}
			}]
		},
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: false
		}
	}
};

var co2Gauge = new RadialGauge({
  renderTo: 'co2Gauge'
});

var coGauge = new RadialGauge({
	renderTo: 'coGauge'
});

var hcGauge = new RadialGauge({
	renderTo: 'hcGauge'
});

var ncxGauge = new RadialGauge({
	renderTo: 'ncxGauge'
});

var o2Gauge = new RadialGauge({
	renderTo: 'o2Gauge'
});

var ceGauge = new RadialGauge({
	renderTo: 'ceGauge'
});

var tempGauge = new LinearGauge({
	renderTo: 'tempGauge',
    units: "°C",
    minValue: 0,
    startAngle: 90,
    ticksAngle: 180,
    maxValue: 100,
    majorTicks: [
        "0",
        "20",
        "40",
        "60",
        "80",
        "100"
    ],
    minorTicks: 2,
    strokeTicks: true,
    highlights: [
        {
            "from": 60,
            "to": 100,
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
    value: 35
})


function getLiveGasData(chart){
  $.ajax({
    url: '/get_real_live_gas_data',
    success: function(response) {
		console.log(response);
		if(response['flag'] == 1){
			co2Gauge.value = Math.abs(parseFloat(response[1]));
			coGauge.value = Math.abs(parseFloat(response[0]));
			hcGauge.value = Math.abs(parseFloat(response[5]));
			ncxGauge.value = Math.abs(parseFloat(response[3]));
			o2Gauge.value = Math.abs(parseFloat(response[2]));
			ceGauge.value = Math.abs(parseFloat(response[4]));
			tempGauge.value = Math.abs(parseFloat(response[6]));
	
			for(i = 0; i <3; i ++){
			  n = i.toString();
			  chart.config.data.datasets[i].data.push({
				x: Date.now(),
				y: response[i]
			  })
			}
		}
    },
    error: function(error) {
        console.log(error);
    }
});
}

$(document).ready(function(){
	var ctx = document.getElementById('gasLineChart').getContext('2d');
	window.myChart = new Chart(ctx, config);
	co2Gauge.draw();
	coGauge.draw();
	hcGauge.draw();
	ncxGauge.draw();
	o2Gauge.draw();
	ceGauge.draw();
	tempGauge.draw();
	var canvasTemp = $('#tempGauge');
    canvasTemp.css("width", '100%');
    canvasTemp.css("height", '100%'); 
}); 

$(window).on('resize', function(){
    resizeGasCanvas();
});

function resizeGasCanvas(){
    var canvasCo2 = $('#co2Gauge');
    canvasCo2.css("width", '100%');
	canvasCo2.css("height", '100%'); 
	
	var canvasCO = $('#coGauge');
    canvasCO.css("width", '100%');
	canvasCO.css("height", '100%'); 
	
	var canvaso2 = $('#o2Gauge');
    canvaso2.css("width", '100%');
	canvaso2.css("height", '100%'); 
	
	var canvashc = $('#hcGauge');
    canvashc.css("width", '100%');
	canvashc.css("height", '100%'); 
	
	var canvasNCX = $('#ncxGauge');
    canvasNCX.css("width", '100%');
	canvasNCX.css("height", '100%'); 
	
	var canvasCE = $('#ceGauge');
    canvasCE.css("width", '100%');
	canvasCE.css("height", '100%'); 
	
	var canvasTemp = $('#tempGauge');
    canvasTemp.css("width", '100%');
    canvasTemp.css("height", '100%'); 
}











