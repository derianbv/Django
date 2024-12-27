############################ VISTAS ##################################################################################33
"""

Las vistas son esencialemente, funciones que reciben un solicitud web y devuelven una respuesta web, las podemos setear así:

IN( Web request: GET,POST,UPDATE,DELETE) ---> f(x) -----> OUT(Web response: String, JSON/XML, HTML, error)
por eso se setean como: def vista(request)

1. creando una app: 

python manage.py startapp firstapp

2. En firstapp/views.py:
"""
from django.http import HttpResponse #Esta clase ayuda a devolver una respuesta Http desde la fx

def home(request): #request como parámetro es la solicitud del usuario
    return HttpResponse("¡Hola, mundo! Esta es la página principal de firstapp.")


"""
Parámetros que recibe HttpResponse(content, content_type, status, reason, charset, headers)

1. content (str, bytes, or iterable):
El contenido de la respuesta. Puede ser una cadena de texto, bytes o un iterable que genere cadenas de texto o bytes.
Ejemplo: HttpResponse("Hello, world!")

2.content_type (str, opcional):

Especifica el tipo de contenido de la respuesta. Por defecto, es 'text/html'.
Ejemplo: HttpResponse("Hello, world!", content_type="text/plain")

3.status (int, opcional):

El código de estado HTTP de la respuesta. Por defecto, es 200.
Ejemplo: HttpResponse("Not Found", status=404)

4. reason (str, opcional):

La razón de la respuesta HTTP. Por defecto, se basa en el código de estado.
Ejemplo: HttpResponse("Not Found", status=404, reason="Not Found")

5. charset (str, opcional):

El conjunto de caracteres (charset) de la respuesta. Por defecto, es 'utf-8'.
Ejemplo: HttpResponse("Hello, world!", content_type="text/html", charset="utf-8")

6.headers (dict, opcional):

Un diccionario de encabezados HTTP que se agregarán a la respuesta.
Ejemplo: HttpResponse("Hello, world!", headers={"Custom-Header": "value"})
"""
    
"""
3. Ahora es necesario configurar la URL de la vista en firstapp/urls.py:
"""

from django.urls import path #path crea las url 
from . import views #acá llamo a firstapp/views.py

#Urlpatterns es una lista de las url seteadas:
urlpatterns = [
    path('', views.home, name='home'),  # '' significa que será la url vacía, luego se llama a la función views.home y esta define el comportamiento de la vista
]

"""
Estos son los parámetros que recive path(route #no lleva / al comienzo , view #no lleva fx() parentesis porque se llama a la fx pero no se ejecuta, kwargs=None, name=None)!!!!!!!!!!!!!!!!!
"""


-route: Ejemplo: 'posts/<int:id>/' acá el sistema detecta post/ ademas de las variables que se pasen por url. 
-view: Si la URL coincide se pasa la función para iniciar con su operación. 
-kwargs (dict, opcional): Es un diccionario de argumentos adicionales que se pasan a la vista. Estos argumentos no se extraen de la URL, sino que se definen estáticamente en el diccionario.
Ejemplo: {'foo': 'bar'} pasará el argumento foo con el valor 'bar' a la vista.
-name (str, opcional):Es una cadena de texto que nombra la ruta. Este nombre se puede utilizar para referenciar la URL en otras partes de Django, como en plantillas o redirecciones. Es útil para generar URLs de forma dinámica.
Ejemplo: name='post-detail'.

"""
4. Ahora en mi proyecto: mi_proyecto/urls.py debo incluir las urls de mi app: 


from django.contrib import admin
from django.urls import path, include #ACA

#Baicamente le digo que le añada el folder fisrtapp/ a mi pagina web, y este llama a todas las fx que yo haya seteado en firstapp/urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include('firstapp.urls')), #ACA
]



