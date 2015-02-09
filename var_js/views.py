import json
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

'''Vista que obtiene la clave a traves de ajax'''
@csrf_exempt
def get_cache_dj_var_js(request):

	try:
		#Obtengo el key
		key = request.POST['key']

		#Obtiene l valor
		pyvar = DjVarJs()
		valor = pyvar.get(key, request)

		#Si es un diccionario convierto a json
		if type(valor) is dict:
			valor = json.dumps(valor, ensure_ascii=False)

	except Exception:
		valor = ""

	return HttpResponse(valor)

'''
	Clase que se encarga de setear en cache una 
	clave-valor para luego leerla a traves de ajax
'''
class DjVarJs(object):
	
	'''
		Seteo la variable en cache
		PARAMETERS: Variable: Variable a setear
					Key: Clave de la cache
					request: Request de la vista para obtener el sessionid
	'''
	def set(self, key, var_set, request):

		try:
			#Salt unique del key
			salt = request.COOKIES['sessionid']
			#Seteo el key en cache
			cache.set(key + "_" + salt, var_set)
		except ExceptionPyVarJs:
			raise ExceptionPyVarJs("Error when setting the key cache")

	'''
		Obtiene una key desde la cache
		PARAMETERS: Key: Clave de la cache
		request: Request de la vista para obtener el sessionid
	'''
	def get(self, key, request):

		try:
			#Salt unique del key
			salt = request.COOKIES['sessionid']
			#Retorno el valor desde la cache
			valor = cache.get(key + "_" + salt)
		except ExceptionPyVarJs:
			raise ExceptionPyVarJs("Error when getting the key cache")

		return valor


''' Clase que crea una excepcion PyVarJS '''
class ExceptionPyVarJs(Exception):
	
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


		