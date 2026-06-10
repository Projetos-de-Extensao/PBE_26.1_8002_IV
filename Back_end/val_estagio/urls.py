from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AlunoViewSet, SecretariaViewSet, CoordenadorViewSet, CursoViewSet, EmpresaViewSet, TceViewSet, RelatorioSemestralViewSet, EstagioViewSet


class PublicApiRootRouter(DefaultRouter):
    APIRootView = type(
        'APIRootView',
        (DefaultRouter.APIRootView,),
        {'permission_classes': [AllowAny]},
    )


router = PublicApiRootRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'secretarias', SecretariaViewSet)
router.register(r'coordenadores', CoordenadorViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'tces', TceViewSet)
router.register(r'relatorios', RelatorioSemestralViewSet)
router.register(r'estagios', EstagioViewSet)



urlpatterns = [
    
path('', include(router.urls)),

]
