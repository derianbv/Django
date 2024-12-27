################################################  Admin ####################################################
## EPP: Sirve para manipular la base de datos sin necesidad de usar ORM

#Setearlo----------------------------------------------------------------------

# 1. Create super user: 
(linux) 
python3 manage.py createsuperuser

#2. Correr el servidor y agregar la ruta /admin al final de la url 
python3 manage.py runserver

#3. Haber creado los modelos en models.py, y luego añadirlos como modelos admin: 

from django.contrib import admin

admin.site.register(Course)
admin.site.register(Instructor)

#Esto nos dará unos campos (de los atributos de la clase) para añadir en la página, sin embargo, si queremos setear más campos configurables tenemos que crear una clase Admin del modelo:
#/

