from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio
from .serializers import EmpresaSerializer, UsuarioSerializer, AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, CursoSerializer, TceSerializer, RelatorioSemestralSerializer, EstagioSerializer
from choices import StatusDocumento

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

    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_tce(self, request, pk=None):
        tce = self.get_object()

        if tce.status == StatusDocumento.APROVADO:
            return Response({'detail': 'TCE já está aprovado.'}, status=400)
        
        tce.se_aprovar()

        serializer = self.get_serializer(tce)

        return Response({'detail': 'TCE aprovado com sucesso.'}, status=200)
    

    @action(detail=True, methods=['post'], url_path='reprovar')
    def reprovar_tce(self, request, pk=None):
        tce = self.get_object()

        if tce.status == StatusDocumento.REPROVADO:
            return Response({'detail': 'TCE já está reprovado.'}, status=400)
        
        tce.se_reprovar()

        serializer = self.get_serializer(tce)

        return Response({'detail': 'TCE reprovado com sucesso.'}, status=200)


class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.select_related(
        'coordenador__usuario',
        'estagio'
    )
    serializer_class = RelatorioSemestralSerializer

    
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_relatorio(self, request, pk=None):
        relatorio = self.get_object()

        if relatorio.status == StatusDocumento.APROVADO:
            return Response({'detail': 'Relatório já está aprovado.'}, status=400)
        
        relatorio.se_aprovar()

        serializer = self.get_serializer(relatorio)

        return Response({'detail': 'Relatório aprovado com sucesso.'}, status=200)
    

    @action(detail=True, methods=['post'], url_path='reprovar')
    def reprovar_relatorio(self, request, pk=None):
        relatorio = self.get_object()

        if relatorio.status == StatusDocumento.REPROVADO:
            return Response({'detail': 'Relatório já está reprovado.'}, status=400)
        
        relatorio.se_reprovar()

        serializer = self.get_serializer(relatorio)

        return Response({'detail': 'Relatório reprovado com sucesso.'}, status=200)


class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.select_related(
        'empresa'
    )
    serializer_class = EstagioSerializer