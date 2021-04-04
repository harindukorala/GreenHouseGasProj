function displayGasBarChart() {
    var data = {
        labels: [],
        datasets: [
            {
                label: "Average C02% Emiision per day",
                backgroundColor: "rgb(255, 99, 132)",
                borderColor: "rgb(255, 99, 132)",
                data: []
            },
            {
                label: "Average C0% Emiision per day",
                backgroundColor: "rgb(54, 162, 235)",
                borderColor: "rgb(54, 162, 235)",
                data: []
            },
            {
              label: "Average 02% Emiision per day",
              backgroundColor: "rgb(153, 102, 255)",
              borderColor: "rgb(153, 102, 255)",
              data: []
          }
          ]
    };

    var options = {
      scales: {
          xAxes: [{
            time: {
              unit: 'Date'
            },
            gridLines: {
              display: false
            },
            ticks: {
              maxTicksLimit: 6
            },
            scaleLabel: {
                display: true,
                labelString: 'Date'
            }
          }],
          yAxes: [{
            ticks: {
              min: 0,
              max: 25,
              maxTicksLimit: 5
            },
            gridLines: {
              color: "rgba(0, 0, 0, .125)",
            },
            scaleLabel:{
                display: true,
                labelString: 'Avg Gas emmision per day'
            }
          }],
        },
        legend: {
          display: true
        }
   };

    getGasData(data, options);

  };

  function getGasData(data, options){
    $.ajax({
        url: '/get_avg_gas_data',
        success: function(responses) {
          for( var item in responses){
            data.labels.push(responses[item].time_stamp)
            for(i = 0; i <3; i ++){
              n = i.toString();
              data.datasets[i].data.push(responses[item][n])
            }
          }
          var ctx = document.getElementById("gasBarChart");

          var barChart = new Chart(ctx, {
              type: 'bar',
              data:data,
              options: options
          });
        },
        error: function(error) {
            console.log(error);
        }
    });
}
  
  $(document).ready(function(){

    displayGasBarChart();
}); 