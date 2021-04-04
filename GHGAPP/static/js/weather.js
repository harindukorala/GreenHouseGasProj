function getWeatherData(){
    $.ajax({
        url: '/get_weather_data',
        success: function(responses) {
            var temp = responses['temp'];
            var pressure = responses['pressure'];
            var humidity = responses['humidity'];
            var uvi = responses['uvi'];
            var wind_speed = responses['wind_speed'];

          var weatherTemp = document.getElementById("weatherTemp");
          var weatherHumidity = document.getElementById("weatherHumidity");
          var weatherPressure = document.getElementById("weatherPressure");
          var weatherUVI = document.getElementById("weatherUVI");
          var weatherWindspeed = document.getElementById("weatherWindspeed");

          weatherTemp.innerHTML = temp + "<sup>&deg;</sup>";
          weatherHumidity.innerHTML = humidity;
          weatherPressure.innerHTML = pressure;
          weatherUVI.innerHTML = uvi;
          weatherWindspeed.innerHTML = wind_speed;
          
          //weatherDiv.innerHTML = "<p>Current Temperature :"+ temp + "</p><p>Current Pressure :"+ pressure + "</p><p>Current Humidity :"+ humidity + "</p><p>UVI :"+ uvi + "</p><p>Current wind speed :"+ wind_speed +"</p>"
        },
        error: function(error) {
            console.log(error);
        }
    });
};
  
  $(document).ready(function(){

    getWeatherData();

    setInterval(function() {
		getWeatherData();
	}, 5 * 1000);
}); 