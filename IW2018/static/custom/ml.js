
$(document).ready(function(){

		// Train dataset
    $("#btn_train").click(function() {
			var dataXUrl = $("#data_x_url").val();
			var targetYUrl = $("#target_y_url").val();

			var body = {
				'data_x_url': dataXUrl,
				'target_y_url': targetYUrl
			};

			$.post( "/api/train", body).done(function( data ) {
				$("#result_coef").val(data);
		  });

    });

		// Prediction
		$("#btn_predict").click(function() {
			var dataXUrl = $("#data_x_url").val();
			var targetYUrl = $("#target_y_url").val();
			var features = $("#text_features").val();

      // covert comma seperated value to array
      // var features = featuresString.split(',').map(function(string) {
      //   return parseFloat(string.trim());
      // });

			var body = {
				'data_x_url': dataXUrl,
				'target_y_url': targetYUrl,
				'features': features
			};

			console.log(JSON.stringify(body));

			$.post( "/api/predict", body).done(function( data ) {
		    $("#rmse").val(data);
		  });

    });

		// Preview dataset
		$("#data_x_preview").click(function() {
			var dataXUrl = $("#data_x_url").val();

			var parameters = {
				'path': dataXUrl
			};

			console.log(JSON.stringify(parameters));

			$("#div_x_tb").empty();

			$.get( "/api/preview", parameters).done(function( data ) {

				var dataset = JSON.parse(data);
				var tableHtml = tableHtmlFromDataset(dataset);
				$("#div_x_tb").append(tableHtml);

		  });

    });

		$("#target_y_preview").click(function() {
			var targetYUrl = $("#target_y_url").val();

			var parameters = {
				'path': targetYUrl
			};

			console.log(JSON.stringify(parameters));

			$("#div_y_tb").empty();

			$.get( "/api/preview", parameters).done(function( data ) {

				var dataset = JSON.parse(data);
				var tableHtml = tableHtmlFromDataset(dataset);
				$("#div_y_tb").append(tableHtml);

		  });

    });


		function tableHtmlFromDataset(dataset) {

			 var table = '<table id="data_x_table" class="table table-striped">';

			 var header = "<thead>";
			 var firstRow = dataset[0];

      //  first row is always the header
			 firstRow.forEach(function(column, colIndex, arr1) {
				 header = header + "<th style='width: 55%;' scope='col'>" + column + "</th>";
			 });
			 header = header + "</thead>";
			 table = table + header;

			 var body = "<tbody>";
			 dataset.forEach(function(row, rowIndex, arr) {
         if (rowIndex !== 0) {
           body = body + "<tr>";
           row.forEach(function(column, colIndex, arr1) {
             body = body + "<td>" + column + "</td>";
           });
           body = body + "</tr>";
         }
			 });
			 table = table + body;
			 table = table + "</table>";

			 return table;
		 }
});
