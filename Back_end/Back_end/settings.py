from pathlib import Path

# BASE_DIR define o diretório raiz do projeto. 
# O Path().resolve() encontra o caminho absoluto no seu sistema de arquivos.
BASE_DIR = Path(__file__).resolve().parent.parent

# CHAVE SECRETA: Usada para assinar cookies de sessão e de criptografia
SECRET_KEY = 'django-insecure-pa97q+n8*@z_v_r-khz*-p4mmez#m7antmm&+xt=p2*a-5&9ds'

# DEBUG = True mostra erros detalhados. Deve ser False em produção para evitar o vazamento de dados.
DEBUG = True

# Define quais domínios podem acessar sua aplicação.
ALLOWED_HOSTS = []

# Chave usada para criptografia de campos
FIELD_ENCRYPTION_KEY = 'f5i67XFO7QwR-0t5bzeDxdTHSizHm1Utgjz3jjeI8H8='

# INSTALLED_APPS: Lista de todos os apps habilitados no projeto.
INSTALLED_APPS = [
    'django.contrib.admin',      # Painel administrativo
    'django.contrib.auth',       # Sistema de autenticação
    'django.contrib.contenttypes',
    'django.contrib.sessions',   # Gerenciamento de sessões
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'val_estagio',
    'rest_framework',
    'corsheaders',
]

# MIDDLEWARE: Camada de processamento que intercepta requisições e respostas.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Proteção contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',     # Middleware para liberar o CORS
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['content-type', 'authorization']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

ROOT_URLCONF = 'Back_end.urls'

# Configurações do CORS 
CORS_ALLOW_ORIGINS = ['http://localhost:3000']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['content-type', 'authorization']

ROOT_URLCONF = 'Back_end.urls' # Aponta para o arquivo de rotas principal

# Configuração de templates (HTML)
TEMPLATES = [...] 

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

TIME_ZONE = 'UTC'

# Configuração do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10 # Define 10 itens por página nas suas APIs
}

# Validação de senhas para garantir que o usuário vai criar senhas fortes
AUTH_PASSWORD_VALIDATORS = [...]

# Internacionalização
LANGUAGE_CODE = 'pt-br' # Idioma do sistema
TIME_ZONE = 'UTC'       # Fuso horário
USE_I18N = True
USE_TZ = True           # Usa fuso horário timezone-aware

# Configuração de arquivos estáticos (CSS, JS, Imagens)
STATIC_URL = 'static/'
