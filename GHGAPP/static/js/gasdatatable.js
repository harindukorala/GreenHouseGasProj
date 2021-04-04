$(document).ready(function(){	
	function loadGasData(){
        $.ajax({
            url: '/get_real_live_gas_data_for_table',
            success: function(responseData) {
				console.log(responseData)
				$('#dataTable').DataTable( {
					data : responseData,
					"columns": [
						{ "data": "Timestamp" },
						{ "data": "CO" },
						{ "data": "HC" },
						{ "data": "CO2" },
						{ "data": "O2" },
						{ "data": "NCX" },
						{ "data": "AFR" },
						{ "data": "Lambda"},
						{ "data": "CE" },
						{ "data": "Temp"}
					]
				} );
            },
            error: function(error) {
                console.log(error);
            }
        });
	}
	
	loadGasData();
});
