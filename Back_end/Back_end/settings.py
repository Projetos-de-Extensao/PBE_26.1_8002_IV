from pathlib import Path
from decouple import config
import drf_spectacular



# BASE_DIR define o diretório raiz do projeto. 
BASE_DIR = Path(__file__).resolve().parent.parent
# O Path().resolve() encontra o caminho absoluto no seu sistema de arquivos.
SECRET_KEY = config(
    'SECRET_KEY',
    default='dev-secret-key'
)

FIELD_ENCRYPTION_KEY = config(
    'FIELD_ENCRYPTION_KEY',
    default='f5i67XFO7QwR-0t5bzeDxdTHSizHm1Utgjz3jjeI8H8='
)

DEBUG = config(
    'DEBUG',
    default=True,
    cast=bool
)

# INSTALLED_APPS: Lista de todos os apps habilitados no projeto.
INSTALLED_APPS = [
    'django.contrib.admin',      # Painel administrativo
    'django.contrib.auth',       # Sistema de autenticação
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Gerenciamento de sessões
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'val_estagio',               # Seu app personalizado
    'rest_framework',            # Django REST Framework (API)
    'corsheaders',               # Permite requisições de outros domínios (CORS)
    'drf_spectacular',            # Geração automática de documentação da API
]

# MIDDLEWARE: Camada de processamento que intercepta requisições e respostas.
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # Middleware para liberar o CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Proteção contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configurações do CORS 
CORS_ALLOW_ORIGINS = ['http://localhost:3000']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['content-type', 'authorization']

ROOT_URLCONF = 'Back_end.urls' # Aponta para o arquivo de rotas principal

# Configuração de templates (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 

WSGI_APPLICATION = 'Back_end.wsgi.application'

# BANCO DE DADOS: Por padrão usa SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Define que você está usando um modelo de usuário customizado em vez do padrão do Django
AUTH_USER_MODEL = 'val_estagio.Usuario'

# Configuração do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20, # Define 20 itens por página nas suas APIs

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', # Para gerar documentação automática

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API de Validação de Estágios',
    'DESCRIPTION': 'Documentação da API do sistema de validação de estágios',
    'VERSION': '1.0.0',
}

# Validação de senhas para garantir que o usuário vai criar senhas fortes
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'pt-br' # Idioma do sistema
TIME_ZONE = 'UTC'       # Fuso horário
USE_I18N = True
USE_TZ = True           # Usa fuso horário timezone-aware

# Configuração de arquivos estáticos (CSS, JS, Imagens)
STATIC_URL = 'static/'
