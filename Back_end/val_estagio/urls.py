from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AlunoViewSet, SecretariaViewSet, CoordenadorViewSet, CursoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'secretarias', SecretariaViewSet, basename='secretaria')
router.register(r'coordenadores', CoordenadorViewSet, basename='coordenador')
router.register(r'cursos', CursoViewSet, basename='curso')



urlpatterns = [
    
path('', include(router.urls)),

]