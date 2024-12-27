################################################  Admin ####################################################
## EPP: Sirve para manipular la base de datos sin necesidad de usar ORM

#Setearlo----------------------------------------------------------------------

# 1. Create super user: 
(linux) 
python3 manage.py createsuperuser

#2. Correr el servidor y agregar la ruta /admin al final de la url 
python3 manage.py runserver

#3. Haber creado los modelos en models.py, y luego añadirlos como modelos admin en admin.py: 

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=30, default='online course')
    image = models.ImageField(upload_to='course_images/')
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(null=True)
    instructors = models.ManyToManyField(Instructor)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment')
    total_enrollment = models.IntegerField(default=0)
    is_enrolled = False





from django.contrib import admin

admin.site.register(Course)
admin.site.register(Instructor)

#Esto nos dará unos campos (de los atributos de la clase) para añadir en la página, sin embargo, si queremos setear más campos configurables tenemos que crear una clase Admin del modelo:
# en /models.py:

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description'] #Acá pasamos las columnas de la clase original para que sean editables 

#A lo de arriba le pasamos como segundo parámetro la clase admin: 
admin.site.register(Course, CourseAdmin)

##--------------------------------------------- Inline -----------------------------------------------------------------
#Sirve para crear pestañas de en dónde pueda editar o añardir dos modelos diferentes que estén relacionados (por Fk): 
#. 1 Se debe crear una clase inLine para lo que quiero "apendizar": 


## /en admin.py
class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5 # Número de campos para añadir rows .

#2. Luego en la clase admin del modelo al que voy a apendizar pongo esto: 

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline] # inlines y le paso las clases que le quiera pegar. 


