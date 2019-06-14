# Copyright 2019
#
# Workshop Ninja Python

import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# TODO: Asignamos a la variable el ID del proyecto
PROJECT_ID = 'workshop-ninja-python'

# TODO: Establecemos el nombre del bucket asi como tamaños máximos y extensiones permitidas
CLOUD_STORAGE_BUCKET = 'workshop-ninja-python.appspot.com'
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
