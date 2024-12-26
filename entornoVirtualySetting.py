######################### Entorno virtual ####################################
'''
Sirve para montar una maquina virtual local, es decir, otro OS en dónde puedo descargar las versiones que necesite y si rompo algo pues se rompe solo en este contexto,
si descargo cosas de manera global puede que rompa ciertos proyectos que solo sirven con ciertas versiones de los programas 



|-----------------------|
|   Sistema Operativo   | <-- Sistema principal
|-----------------------|
      |      |      |
      v      v      v
   Entorno1 Entorno2 Entorno3  <-- Cada proyecto con sus propias dependencias

   
'''


########### Cosas necesarias para correr django ###################
'''
(Linux)
pip install --upgrade distro-info
pip3 install --upgrade pip==23.2.1
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

#Se crea primero el entorno virtual y después se installa Django, esto crea carpetas para hacer funcionar al entorno virtual  de django

pip install Django
django-admin startproject firstproject 

#Luego, instalo django e inicio mi proyecto nuevo, se crea la carpeta (first proyect) 
#!! PRIMERO SE CREA EL PROYECYO Y LUEGO LAS APPS QUE TENGA: 


<nombre_proyecto>/
├── <nombre_proyecto>/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py


ahora: 

python3 manage.py startapp firstapp

#esto crea una app nueva dento del proyecto con estos archivos: 

<nombre_app>/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

#El ejemplo completo sería: 

myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

Los proyectos pueden tener varias apps, cada app puede manejar cosas de lógica o cosas así. 

Luego para correr el server tengo que: 

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


------------------------------------------------
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 26, 2024 - 21:08:31
Django version 5.1.4, using settings 'firstproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
----------------------------------------------------------------



'''
