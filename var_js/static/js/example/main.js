$(document).ready(function(){

	var valor = DjVarJs.getKey("variable");
	$("#key_js").text(valor);

	var arr = DjVarJs.getDict("diccionario_django");
	$("#dict_js").text("Clave1: " + arr['clave1'] + ", Clave2: " + arr['clave2'] + ", Clave3: " + arr['clave3']);



});