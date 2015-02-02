django-var-js/README.rst
======
Var-js
======

Var-js is a simple Django application that allows communication 
variables from the server to the client.

Requirements
-----------

JQuery

Quick start
-----------

1. Include the var-js URLconf in your project urls.py like this::

	url(r'^', include('var_js.dj_var_js.urls')),

2. In view.py::

   def example(request):
      #Values
      variable = "To JavaScript"
      dicc = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
		
      #Instance of class DjVarJs
      pyvar = DjVarJs()

      #Set values 
      pyvar.set("variable", variable , request)
      pyvar.set("dicc_django", dicc, request)

      return render_to_response('example.html', context_instance=RequestContext(request))

3. In the template::
	
   <!DOCTYPE html>
   <html>
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
     <script src='{{STATIC_URL}}js/var_js/djvarjs.js'></script>
     <script src='{{STATIC_URL}}js/example/main.js'></script>
   </head>
   <body>
     <h1>App Django-var-js</h1>
     <label id="key_js"></label>
     <br>
     <label id="dict_js"></label>
   <body>
   </html>

4. In the file .js::

     var valor = DjVarJs.getKey("variable");
     $("#key_js").text(valor);

     var arr = DjVarJs.getDict("dicc_django");
     $("#dict_js").text("Clave1: " + arr['clave1'] + ", Clave2: " + arr['clave2'] + ", Clave3: " + arr['clave3']);

5. Visit http://127.0.0.1:8000/example/
