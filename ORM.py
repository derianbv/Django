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

from django.db import models

class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(null=False, max_length=30, default='john') #CharField setea el datatype, luego los parámetros de esta fx serán las otras constraint.
    # CharField for user's last name
    last_name = models.CharField(null=False, max_length=30, default='doe')
    # CharField for user's date for birth
    dob = models.DateField(null=True)


############################################### Settings ##############################################################

########### Migraciones (subir a la base de datos) ---------------------------------------------------------------------------
Linux:
python3 manage.py makemigrations orm
- Ayuda a crear un archivo en el proyecto con las migraciones que hago a la base de datos
- Para ver esta carpeta: python3 manage.py sqlmigrate orm 0001

!!!!!!!!!!!! Hay que hacerle commit a las cosas de la base de datos (muy silimar a hacer commits con git-linux) 

python3 manage.py makemigrations # crea un nuevo archivo de migraciones (stagin area)

python3 manage.py migrate # le hace commit al archivo 
'''
