
############################################### Autorización ############################################## 
#Todo empieza en los modelos usuarios, que gestiona parametros como username, password, first_name, last_name, email, roles, is_active 

##### Pasos ########################: 

# 1. Crear un super user: 

python3 manage.py createsuperuser

# Se añanden al html cosas que solo aparezcan si el usuario está verificado:

{% if user.is_authenticated %}
    <div class="rightalign">
        <div class="dropdown">
            <button class="dropbtn">{{user.first_name}}</button>
            <div class="dropdown-content">
                <a href="{% url 'onlinecourse:logout' %}">Logout</a>  #Apunta a una función post que tiene path(...,..., name=logout) 
            </div>
        </div>
    </div>
    {% else %}
    <div class="rightalign">
        <div class="dropdown">
            <button class="dropbtn">Visitor</button>
            <div class="dropdown-content">
                <a href="{% url 'onlinecourse:login' %}">Login</a> #Apunta a una función post que tiene path(...,..., name=login) 
            </div>
        </div>
    </div>
{% endif %}

#Hay que cambiar las views.py: 

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('onlinecourse:popular_course_list')

# y también las url, 
