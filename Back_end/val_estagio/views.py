from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsAluno, IsSecretaria, IsCoordenador
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio
from .serializers import EmpresaSerializer, UsuarioSerializer, AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, CursoSerializer, TceSerializer, RelatorioSemestralSerializer, EstagioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.select_related(
        'usuario',
        'curso'
    )
    serializer_class = AlunoSerializer

class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.select_related(
        'usuario'
    )
    serializer_class = SecretariaSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.select_related(
        'usuario'
    )
    serializer_class = CoordenadorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class TceViewSet(viewsets.ModelViewSet):
    queryset = Tce.objects.select_related(
        'aluno__usuario',
        'secretaria'
    )
    serializer_class = TceSerializer

    def get_permissions(self):
        if self.action in ['aprovar', 'reprovar']:
            return [IsSecretaria()] 
        return [IsSecretaria() | IsAluno()]

class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.select_related(
        'coordenador__usuario',
        'estagio'
    )
    serializer_class = RelatorioSemestralSerializer

    def get_permissions(self):
        if self.action in ['aprovar', 'reprovar']:
            return [IsCoordenador()]
        return [IsCoordenador() | IsAluno()]

class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.select_related(
        'empresa'
    )
    serializer_class = EstagioSerializer
