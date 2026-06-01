"""
Configuração WSGI para o projeto Back_end.

Este arquivo expõe o callable (objeto chamável) WSGI como uma variável 
de nível de módulo chamada ``application``.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

# Importa a função que inicializa a interface WSGI do Django
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente para que o Django saiba quais configurações utilizar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Back_end.settings')

# Cria o objeto 'application'. 
# Este objeto é a interface de comunicação entre o servidor web e o seu código Django.
application = get_wsgi_application()