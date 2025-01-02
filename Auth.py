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
                <a href="{% url 'onlinecourse:logout' %}">Logout</a>
           </div>
       </div>
</div>
{% endif %}
