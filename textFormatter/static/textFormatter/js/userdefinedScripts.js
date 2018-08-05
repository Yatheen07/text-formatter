function fillData(data){
	document.getElementById('target').innerHTML = "Formatted Text Result: "+ data;
}


$(document).ready(function(){
	
    $("#inputlg").on("input",function(){
		var inputData = $("#inputlg").val();
        
		$.ajax({
			url:'http://192.168.43.35:7345/bold/',
			method:'POST',
			data:{'Data':inputData},
			dataType:'text',
			success: function(data){
				fillData(data);
			},
			error: function(jqXHR,exception){
				alert("Status code: "+jqXHR.status);
			}
		});
		
		
    });
});

