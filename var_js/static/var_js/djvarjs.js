
var DjVarJs = {
	version: "1.0",
	/*Obtiene una variable desde django*/
	getKey: function(key){

		var valor;
		$.ajax({
		    url:'/get_cache_dj_var_js/',
		    type: "POST",
		    async: false,
		    data: {key: key},
		    success:function(response){
		    	valor = response;
		    },
		    error:function (xhr, textStatus, thrownError){
		    	console.log(thrownError);
		    }
		});

		return valor;
	},
	/*Obtiene un diccionario desde django*/
	getDict: function(key){

		var valor;
		$.ajax({
		    url:'/get_cache_dj_var_js/',
		    type: "POST",
		    async: false,
		    data: {key: key},
		    success:function(response){
		    	obj = JSON.parse(response);
		    	valor = obj;
		    },
		    error:function (xhr, textStatus, thrownError){
		    	console.log(thrownError);
		    }
		});

		return valor;

	}
};
