from pathlib import Path
from decouple import config
import drf_spectacular



# BASE_DIR define o diretório raiz do projeto. 
BASE_DIR = Path(__file__).resolve().parent.parent
# O Path().resolve() encontra o caminho absoluto no seu sistema de arquivos.


def config_bool(name, default=False):
    try:
        return config(name, default=default, cast=bool)
    except ValueError as exc:
        value = str(config(name, default=default)).strip().lower()

        if value in {'release', 'prod', 'production'}:
            return False

        if value in {'dev', 'development'}:
            return True

        raise ValueError(
            f"Valor inválido para {name}: {value!r}. Use True/False, dev ou release."
        ) from exc


SECRET_KEY = config(
    'SECRET_KEY',
    default='dev-secret-key'
)

FIELD_ENCRYPTION_KEY = config(
    'FIELD_ENCRYPTION_KEY'
)

DEBUG = config_bool(
    'DEBUG',
    default=False
)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=lambda value: [host.strip() for host in value.split(',') if host.strip()]
)

# INSTALLED_APPS: Lista de todos os apps habilitados no projeto.
INSTALLED_APPS = [
    'django.contrib.admin',      # Painel administrativo
    'django.contrib.auth',       # Sistema de autenticação
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Gerenciamento de sessões
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'val_estagio',               # Seu app personalizado
    'rest_framework',            # Django REST Framework (API)
    'corsheaders',               # Permite requisições de outros domínios (CORS)
    'drf_spectacular',            # Geração automática de documentação da API
    'django_filters',           # Filtros para a API
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

REST_FRAMEWORK = {
    # Autenticação e Permissões
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    # Paginação
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,  # Define 20 itens por página
    
    # Documentação Automática (drf-spectacular)
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
    # Filtros
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],

    'DEAFULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '50/hour',  # Limite para usuários anônimos
        'user': '500/hour', # Limite para usuários autenticados
    }
}

# Configurações do CORS 
CORS_ALLOW_ORIGINS = config(
    'CORS_ALLOW_ORIGINS',
    default='http://localhost:3000',
    cast=lambda v: [s.strip() for s in v.split(",")]
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['content-type', 'authorization']
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'Back_end.urls'

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

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

# Configuração do Django REST Framework


SPECTACULAR_SETTINGS = {
    'TITLE': 'API de Validação de Estágios',
    'DESCRIPTION': 'Documentação da API do sistema de validação de estágios',
    'VERSION': '1.0.0',
}

# Internacionalização
USE_I18N = True
USE_TZ = True           # Usa fuso horário timezone-aware

# Configuração de arquivos estáticos (CSS, JS, Imagens)
STATIC_URL = 'static/'
