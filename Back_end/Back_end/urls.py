from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (
   SpectacularAPIView,
   SpectacularSwaggerView,
   SpectacularRedocView,
)

# Lista de rotas (urlpatterns) que o Django irá processar
urlpatterns = [
    # Direciona todas as requisições que começam com 'api/' para o arquivo 
    # de rotas específico dentro do app 'val_estagio'
    path('api/', include('val_estagio.urls')),
    
    # Rota padrão do painel administrativo do Django
    path('admin/', admin.site.urls),  

    path('api/auth/login/', obtain_auth_token, name='login'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Interface interativa (Swagger) para testar os endpoints
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Interface alternativa de documentação (Redoc)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]