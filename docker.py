################################### docker.py #################################################

######################### Setting ##########################################
# 1. project/settings.py: 
ALLOWED_HOSTS = ['*','.us-south.codeengine.appdomain.cloud']

#2.  in project/: 
(linux) 

pip install pipreqs
pipreqs . #busca en el directorio actual los requerimientos para correr la app y los guarda en requirements 

#Esto va a crear un archivo nuevo requirements.txt que tendrá lo necesario para mi app
