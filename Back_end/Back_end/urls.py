from django.contrib import admin
from django.urls import path, include

# IMPORTANTE: Importamos a nossa View customizada em vez da padrão
from val_estagio.views import CustomAuthToken 

from drf_spectacular.views import (
   SpectacularAPIView,
   SpectacularSwaggerView,
   SpectacularRedocView,
)

urlpatterns = [
    path('api/', include('val_estagio.urls')),
    path('admin/', admin.site.urls),  

    
    path('api/auth/login/', CustomAuthToken.as_view(), name='login'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]