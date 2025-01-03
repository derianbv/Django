''' 

############################# Name Spacin ##############################################3



project/
    ├── manage.py
    ├── project/
    │    ├── settings.py
    │    ├── urls.py
    ├── myapp/                     # Carpeta de la aplicación
    │    ├── views.py
    │    ├── urls.py
    │    └── templates/            # Carpeta de plantillas
    │         └── myappLOL/           # Subcarpeta específica de la aplicación #ACA HAY DOS myapp/ pero esta es para que el padre de cada template sea my app
    │              └── index.html  # Plantilla específica de la app

#para llamar a una template se deberá usar:myappLOL.template.html, esta es la utilidad: tener más claridad


#Confi----------------
#En settings.py: 
settings.py, el apartado TEMPLATES esté configurado con APP_DIRS=True. Esto le indica a Django que busque automáticamente plantillas dentro de la subcarpeta templates/ de cada aplicación:

'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # Otros context processors...
            ],
        },
    },
]

'''
Llamada de estas templates dentro de myapp/ 
en urls.py: 

'''
from django.shortcuts import render

def my_view(request):
    return render(request, 'myappLOL/template.html')  # Prefijo + nombre del archivo

'''
HTML'''
<!-- base.html -->
{% include 'myappLOL/template.html' %}





