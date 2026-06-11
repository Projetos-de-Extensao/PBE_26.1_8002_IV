"""
Configuração ASGI para o projeto Back_end.

Este arquivo expõe o callable (objeto chamável) ASGI como uma variável 
de nível de módulo chamada ``application``.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

# Importa a função necessária para configurar a aplicação ASGI do Django
from django.core.asgi import get_asgi_application

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE' para apontar para o arquivo de configurações do seu projeto. 
# Isso garante que o Django saiba quais configurações carregar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Back_end.settings')

# Cria a instância da aplicação ASGI. 
# Esta variável 'application' é o que o servidor (como o Uvicorn ou Daphne) 
# utilizará para rodar o seu projeto de forma assíncrona.
application = get_asgi_application()