################################################  Admin ####################################################
## EPP: Sirve para manipular la base de datos sin necesidad de usar ORM

#Setearlo----------------------------------------------------------------------

# 1. Create super user: 
(linux) 
python3 manage.py createsuperuser

#2. Correr el servidor y agregar la ruta /admin al final de la url 
python3 manage.py runserver

#3. Haber creado los modelos en models.py, y luego añadirlos como modelos admin: 

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
    fields = ['pub_date', 'name', 'description'] #Acá pasamos las columnas de la clase original para 
