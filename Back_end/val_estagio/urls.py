from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AlunoViewSet, SecretariaViewSet, CoordenadorViewSet, CursoViewSet, EmpresaViewSet, SeguradoraViewSet, TceViewSet, RelatorioSemestralViewSet, EstagioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'secretarias', SecretariaViewSet)
router.register(r'coordenadores', CoordenadorViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'seguradoras', SeguradoraViewSet)
router.register(r'tces', TceViewSet)
router.register(r'relatorios', RelatorioSemestralViewSet)
router.register(r'estagios', EstagioViewSet)



urlpatterns = [
    
path('', include(router.urls)),

]