############################ VISTAS ##################################################################################33
"""

Las vistas son esencialemente, funciones o clases que reciben un solicitud web y devuelven una respuesta web, las podemos setear así:

IN( Web request: GET,POST,UPDATE,DELETE) ---> f(x) -----> OUT(Web response: String, JSON/XML, HTML, error)
por eso se setean como: def vista(request)

1. creando una app: 

python manage.py startapp firstapp

2. En firstapp/views.py:
"""
from django.http import HttpResponse #Esta clase ayuda a devolver una respuesta Http desde la fx

def home(request): #request como parámetro es la solicitud del usuario
    return HttpResponse("¡Hola, mundo! Esta es la página principal de firstapp.") # También puede ser render()


"""
Esta funcion retorna una respuesta HTTP.
Parámetros que recibe HttpResponse(content, content_type, status, reason, charset, headers) #Devuelve solo cosas estáticas, no acepta conexto para hacer lógica como: {% for course in course_list %} 

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


Para hacer templates que cambien con el contexto o las variables que les pasamos debemos usar render() que es exclusivo para plantillas html. 

django.shortcuts.render(request, template_name, context=None, content_type=None, status=None, using=None)
a. request (obligatorio) = es el parametro del requereminento que le hizo el cx a la vista. 
b. template_name (obligatorio) = el nombre de la plantilla que vamos a usar, django busca en lals rutas definidas en la setting TEMPLATES de settings.py
c. context = diccionario que contiene variables que se le pasan a la plantilla, como si fueran escritas dentro del html así: {% with variable_name="valor" %} (context = {"variable_name": "valor"}), 
contect_type = especifica el contenido de la respuesta HTTP que genera la vista, por defecto text/html 
d. status = codigo de confirmación que retorna la página 
e. using = el motor de render del html, se jinja2 u otro 

________________ Ejemplo del contexto ____________________________

**** en la vista ------------------

from django.shortcuts import render

"""
def my_view(request):
    context = {
        "username": "Juan",  # Pasamos una variable 'username'
        "is_logged_in": True,  # Indicamos que el usuario está logueado
        "notifications": ["Mensaje 1", "Mensaje 2"],  # Lista de notificaciones
    }
    return render(request, "my_template.html", context)

"""
*** en el html my_template.html-------------------
"""


<!DOCTYPE html>
<html>
<head>
    <title>Ejemplo de Plantilla</title>
</head>
<body>
    <h1>Hola, {{ username }}!</h1> #acá puede sacarlo porque encuentra la variable username que se le pasó por contexto 

    {% if is_logged_in %}
        <p>Estás conectado.</p>
        <ul>
            {% for notification in notifications %}
                <li>{{ notification }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Por favor, inicia sesión.</p>
    {% endif %}
</body>
</html>




#____________________ejemplo 2, llamando a la base de datos para guardar context ___________________________________              


def popular_course_list(request):
    context = {}
    # If the request method is GET
    if request.method == 'GET':
        # Using the objects model manage to read all course list
        # and sort them by total_enrollment descending
        course_list = Course.objects.order_by('-total_enrollment')[:10] #ACÁ llamo a la base de datos 
        # Appen the course list as an entry of context dict
        context['course_list'] = course_list # Acá la append al diccionario context
        return render(request, 'onlinecourse/course_list.html', context)




"""
3. Ahora es necesario configurar la URL de la vista en firstapp/urls.py: ####################### Path #################################

"""

from django.urls import path #path crea las url 
from . import views #acá llamo a firstapp/views.py

#Urlpatterns es una lista de las url seteadas:
urlpatterns = [
    path('', views.home, name='home'),  # '' significa que será la url vacía, luego se llama a la función views.home y esta define el comportamiento de la vista
]

"""
Estos son los parámetros que recive path(route #no lleva / al comienzo , view #no lleva fx() parentesis porque se llama a la fx pero no se ejecuta, kwargs=None, name=None)!!!!!!!!!!!!!!!!!

-route: Ejemplo: 'posts/<int:id>/' acá el sistema detecta post/ ademas de las variables que se pasen por url pero esto debe notarse en la vista (f(x) que procesa la url: def course_details(request, course_id #pasarle el parametro)
-view: Si la URL coincide se pasa la función para iniciar con su operación. 
-kwargs (dict, opcional): Es un diccionario de argumentos adicionales que se pasan a la vista. Estos argumentos no se extraen de la URL, sino que se definen estáticamente en el diccionario.
Ejemplo: {'foo': 'bar'} pasará el argumento foo con el valor 'bar' a la vista.
-name (str, opcional):Es una cadena de texto que nombra la ruta. Este nombre se puede utilizar para referenciar la URL en otras partes de Django, como en plantillas o redirecciones. Es útil para generar URLs de forma dinámica.
Ejemplo: name='post-detail'.

"""


"""
4. Ahora en mi proyecto: mi_proyecto/urls.py debo incluir las urls de mi app: 


"""


from django.contrib import admin
from django.urls import path, include #ACA

#Baicamente le digo que le añada el folder fisrtapp/ a mi pagina web, y este llama a todas las fx que yo haya seteado en firstapp/urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include('firstapp.urls')), #ACA
]



'''

################################################################# Views Clases ####################################################################################






'''

