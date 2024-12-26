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


con la sig estructura: 

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

    Cada archivo da una idea de qué contiene su código interno

'''
