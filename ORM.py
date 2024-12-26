####################################### ORM ####################################################3

'''
La idea general se basa en manejar bases de datos con objetos (ya que son muy similar), entonces Django me deja manipular objetos y de este modo, el Object-Relational Mapping
se encargará de traducir el codigo a SQL, sin importar cuál sea su tipo (sqlite, mysql, etc). 


Para realizar esto, se deben utilizar los modelos de django, que son epp de nombrar tablas. 
EJEMPLO: 


Como sería en Postgres:---------------------------------------------------------------------------

CREATE TABLE User (
    UserID SERIAL PRIMARY KEY, -- SERIAL genera un campo auto-incremental para el ID
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL DEFAULT 'john',
    dob DATE NOT NULL -- Cambié "DATE" a "dob" para mayor claridad y lo marqué como NOT NULL
);



Como es en Django:-----------------------------------------------------------------------------------
#Es importante recalcar que a estas tablas se les asigna un primary key implicito con serial (basicamente añade de manera implicita esto:  id = models.AutoField(primary_key=True))

from django.db import models

class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(null=False, max_length=30, default='john') #CharField setea el datatype, luego los parámetros de esta fx serán las otras constraint.
    # CharField for user's last name
    last_name = models.CharField(null=False, max_length=30, default='doe')
    # CharField for user's date for birth
    dob = models.DateField(null=True)

'''
####################################### Insertar Rows en tablas #######################


# Definimos el modelo Course
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

# Definimos el modelo Project
class Project(models.Model):
    name = models.CharField(max_length=255)
    grade = models.FloatField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  #-------- Relación 1 a m con Course

# Crear una instancia de Course
course_cloud_app = Course(
    name="Cloud Application Development with Database",
    description="Develop and deploy application on cloud"
)
course_cloud_app.save()  # Guardar la instancia en la base de datos (le hace commit)

# Crear una instancia de Project asociada al curso anterior
project_orm = Project(
    name="Object-relational mapping project",
    grade=0.2,
    course=course_cloud_app
)
project_orm.save()  

'''
############################################### Settings ##############################################################

########### Migraciones (subir a la base de datos) ---------------------------------------------------------------------------
Linux:
python3 manage.py makemigrations orm
- Ayuda a crear un archivo en el proyecto con las migraciones que hago a la base de datos
- Para ver esta carpeta: python3 manage.py sqlmigrate orm 0001

!!!!!!!!!!!! Hay que hacerle commit a las cosas de la base de datos (muy silimar a hacer commits con git-linux) 

python3 manage.py makemigrations # crea un nuevo archivo de migraciones (stagin area)

python3 manage.py migrate # le hace commit al archivo 




###################################### Especial variables  ######################################################
from django.db import models
from django.utils.timezone import now


class User(models.Model): 
    first_name = models.CharField(null = False, max_length = 30, default = 'john')
    last_name = models.CharField(null = False, max_length = 30, default = 'john')
    dob = models.DateField(null = True)

    def ___str__(self): #le puedo sobreescribir comportamientos a sus métodos como si fuera una clase normal
        return self.first_name + " " + self.last_name


########################################### Relaciones   ###########################################################
1. RELACIÓN 1:1 : 
-Se puede hacer de manera manual o por herencia. 
    -De manera HERENCIA: ****************************

    class Persona(models.Model): 
        nombre models.charField(max_lenght = 4) 

    class Trabajador (Persona): #Hereda de persona, o sea se le añade implicitamente una FK que apunta al id de Persona
        puesto models.charField(max_lenght = 4) 

Así queda la tabla Trabajador

id	nombre	    puesto
1	Juan Pérez	Ingeniero
2	Ana López	Diseñadora


    -De manera Manual: 

    class Persona(models.Model):
        nombre = models.CharField(max_length=100)

    class Empleado(models.Model): #No hereda, se crea un modelo desde 0 
        persona = models.OneToOneField(Persona, on_delete=models.CASCADE)  #se añada explicitamente la relación 1 a 1. 
        puesto = models.CharField(max_length=50)




2. Relación 1a1 y 1toMany: 

1 to Many-----------------------

class Autor(models.Model):
    nombre = models.CharField(max_length=255) 

class Cancion(models.Model):
    nombre_cancion = models.CharField(max_length=255)  # Nombre de la canción.
    autor = models.ForeignKey(Autor, on_delete=CASCADE) 


Tabla Autor:
id	nombre
1	Juan Pérez
2	Ana López



#Many canciones pueden ser de One autor 
Tabla Cancion:
id	nombre_cancion	autor_id
1	Canción 1	       1
2	Canción 2	       1
3	Canción 3	       2

1 to 1 --------------------------------------------------------------------------------------
-Manera manual (constraint Unique):


class Autor(models.Model):
    nombre = models.CharField(max_length=255) 

class Cancion(models.Model):
    nombre_cancion = models.CharField(max_length=255)  # Nombre de la canción.
    autor = models.ForeignKey(Autor, on_delete=CASCADE, unique=True)  ######## ACÁ ESTÁ LA MAGIA 

-Manera 2 (usando OnetoOne): 


class Autor(models.Model):
    nombre = models.CharField(max_length=255)

class Cancion(models.Model):
    Autor = models.OneToOneField(Autor, on_delete=models.CASCADE)  #Esto añade implicitamente el unique
    nombre_cancion = models.TextField()

id	nombre_cancion	autor_id (autor tiene que ser único) 
1	Canción 1	       1
2	Canción 2	       2
3	Canción 3	       3 


------------------------- Many to Many ----------------------------------------------------------------
#Django crea la tabla intermedia automaticamente (en donde permutan) pero la puedo crear yo si quiero a través de through.

Ejemplo:

class Autor(models.Model):
    nombre = models.CharField(max_length=255)

class Cancion(models.Model):
    nombre_cancion = models.TextField()
    autores = models.ManyToManyField(Autor) #Solo debo poner y Django crea la tabla automaticamente. 

------------
Tabla autor: 
-------------
id	nombre
1	Juan Pérez
2	Ana López

--------------
tabla cancion 
--------------
id	nombre_cancion
1	Balada del programador
2	Canción de 


-------------------------------------
Tabla intermedia app_cancion_autores:
-------------------------------------
id	cancion_id	autor_id
1	  1	        1
2	  1	        2
3	  2	        2


le piedo poner through como parametro si quiero yo crear la tabla: 

autores = models.ManyToManyField(Autor, thorugh='Table_que_yo_cree')



####################### METADATA y Choises #############################################################################


class Learner(User):
------------------------------------------
Estos no son columnas, son meta data que se puede guardar en los modelos, en este caso en concreto sirven para poner restricciones 
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'

    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
-----------------------------------------------------------
    occupation = models.CharField(
        max_length=20,
        choices=OCCUPATION_CHOICES, #El parametro sirve para solo admitir ciertos datos, en este caso los datos serán los que se guardaron en la metadata 
        default=STUDENT
    )

Ya en uso:

learner = Learner(occupation="doctor")  # Error: "doctor" no está en OCCUPATION_CHOICES

'''
