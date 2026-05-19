from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AlunoViewSet, SecretariaViewSet, CoordenadorViewSet, CursoViewSet, EmpresaViewSet, SeguradoraViewSet, TceViewSet, RelatorioSemestralViewSet, EstagioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'secretarias', SecretariaViewSet, basename='secretaria')
router.register(r'coordenadores', CoordenadorViewSet, basename='coordenador')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'empresas', EmpresaViewSet, basename='empresa')
router.register(r'seguradoras', SeguradoraViewSet, basename='seguradora')
router.register(r'tces', TceViewSet, basename='tce')
router.register(r'relatorios', RelatorioSemestralViewSet, basename='relatorio')
router.register(r'estagios', EstagioViewSet, basename='estagio')



urlpatterns = [
    
path('', include(router.urls)),

]