from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAluno, IsSecretaria, IsCoordenador
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio
from .serializers import EmpresaSerializer, UsuarioSerializer, AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, CursoSerializer, TceSerializer, RelatorioSemestralSerializer, EstagioSerializer
from .choices import StatusDocumento

# --- VIEWSET DE USUÁRIOS ---

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD completas
    para usuários do sistema.

    Endpoints gerados automaticamente:
    - Listar usuários
    - Consultar usuário
    - Cadastrar usuário
    - Atualizar usuário
    - Excluir usuário
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsSecretaria()]


# --- VIEWSET DE ALUNOS ---

class AlunoViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para alunos.

    Utiliza select_related para otimizar
    consultas envolvendo:
    - Usuário vinculado
    - Curso vinculado
    """

    queryset = Aluno.objects.select_related(
        'usuario',
        'curso'
    )
    serializer_class = AlunoSerializer

    filterset_fields = [
        'procurando_estagio',
        'curso',
        'periodo'
    ]

    def get_permissions(self):
        if self.action == 'list':
            return [IsSecretaria() | IsCoordenador()]
        if self.action == 'retrieve':
            return [IsSecretaria() | IsCoordenador() | IsAluno()]
        if self.action in ['update', 'partial_update']:
            return [IsSecretaria() | IsAluno()]
        return [IsSecretaria()]

# --- VIEWSET DE SECRETARIAS ---

class SecretariaViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para secretarias.

    Realiza carregamento otimizado do usuário
    relacionado através do select_related.
    """

    queryset = Secretaria.objects.select_related(
        'usuario'
    )
    serializer_class = SecretariaSerializer

    filterset_fields = [
        'usuario'
    ]

    def get_permissions(self):
        return [IsSecretaria()]


# --- VIEWSET DE COORDENADORES ---

class CoordenadorViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para coordenadores.

    Realiza carregamento otimizado do usuário
    relacionado através do select_related.
    """

    queryset = Coordenador.objects.select_related(
        'usuario'
    )
    serializer_class = CoordenadorSerializer

    filterset_fields = [
        'area'
    ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsSecretaria() | IsCoordenador()]
        return [IsSecretaria()]



# --- VIEWSET DE CURSOS ---

class CursoViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD completas
    para cursos cadastrados no sistema.
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsSecretaria()]


# --- VIEWSET DE EMPRESAS ---

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD completas
    para empresas concedentes de estágio.
    """

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    filterset_fields = [
        'cidade',
        'uf'
    ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsSecretaria()]

# --- VIEWSET DE TCE ---

class TceViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para TCE
    (Termo de Compromisso de Estágio).

    Também disponibiliza ações específicas para:
    - Aprovação
    - Reprovação

    Utiliza select_related para otimizar
    consultas dos relacionamentos.
    """

    queryset = Tce.objects.select_related(
        'aluno__usuario',
        'secretaria'
    )
    serializer_class = TceSerializer

    filterset_fields = [
        'status',
        'aluno',
        'secretaria'
    ]


    def get_permissions(self):
        if self.action in ['aprovar_tce', 'reprovar_tce']:
            return [IsSecretaria()]
        if self.action in ['list', 'retrieve']:
            return [IsSecretaria() | IsAluno()]
        if self.action == 'create':
            return [IsAluno() | IsSecretaria()]
        return [IsSecretaria()]
    # --- APROVAR TCE ---
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_tce(self, request, pk=None):
        """
        Aprova um TCE específico.

        Regras:
        - Não permite aprovar um TCE já aprovado.
        - Executa a regra de negócio se_aprovar().
        """
        tce = self.get_object()
        if tce.status == StatusDocumento.APROVADO:
            return Response({'detail': 'TCE já está aprovado.'}, status=400)
        tce.se_aprovar()
        return Response({'detail': 'TCE aprovado com sucesso.'}, status=200)

    @action(detail=True, methods=['post'], url_path='reprovar')
    def reprovar_tce(self, request, pk=None):
        tce = self.get_object()
        if tce.status == StatusDocumento.REPROVADO:
            return Response({'detail': 'TCE já está reprovado.'}, status=400)
        tce.se_reprovar()
        return Response({'detail': 'TCE reprovado com sucesso.'}, status=200)


# --- VIEWSET DE RELATÓRIOS SEMESTRAIS ---

class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para
    relatórios semestrais de estágio.

    Também disponibiliza ações para:
    - Aprovação
    - Reprovação

    Utiliza select_related para otimizar
    consultas dos relacionamentos.
    """

    queryset = RelatorioSemestral.objects.select_related(
        'coordenador__usuario',
        'estagio'
    )
    serializer_class = RelatorioSemestralSerializer
    
    filterset_fields = [
        'status',
        'semestre',
        'estagio',
        'coordenador'
    ]

    def get_permissions(self):
        if self.action in ['aprovar_relatorio', 'reprovar_relatorio']:
            return [IsCoordenador()]
        if self.action in ['list', 'retrieve']:
            return [IsCoordenador() | IsAluno()]
        if self.action == 'create':
            return [IsAluno()]
        return [IsSecretaria()] 

    # --- APROVAR RELATÓRIO ---

    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_relatorio(self, request, pk=None):
        """
        Aprova um relatório semestral.

        Regras:
        - Não permite aprovar um relatório já aprovado.
        - Executa a regra de negócio se_aprovar().
        """

        relatorio = self.get_object()

        if relatorio.status == StatusDocumento.APROVADO:
            return Response({'detail': 'Relatório já está aprovado.'}, status=400)

        relatorio.se_aprovar()

        serializer = self.get_serializer(relatorio)

        return Response({'detail': 'Relatório aprovado com sucesso.'}, status=200)

    # --- REPROVAR RELATÓRIO ---

    @action(detail=True, methods=['post'], url_path='reprovar')
    def reprovar_relatorio(self, request, pk=None):
        """
        Reprova um relatório semestral.

        Regras:
        - Não permite reprovar um relatório já reprovado.
        - Executa a regra de negócio se_reprovar().
        """

        relatorio = self.get_object()

        if relatorio.status == StatusDocumento.REPROVADO:
            return Response({'detail': 'Relatório já está reprovado.'}, status=400)

        relatorio.se_reprovar()

        serializer = self.get_serializer(relatorio)

        return Response({'detail': 'Relatório reprovado com sucesso.'}, status=200)


# --- VIEWSET DE ESTÁGIOS ----

class EstagioViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza operações CRUD para estágios.

    Utiliza select_related para otimizar
    consultas envolvendo a empresa vinculada.
    """

    queryset = Estagio.objects.select_related(
        'empresa',
        'tce'
    )
    serializer_class = EstagioSerializer

    filterset_fields = [
        'empresa',
        'tce'
    ]

    def get_permissions(self):
        if self.action == 'adicionar_relatorio':
            return [IsAluno()]
        if self.action in ['list', 'retrieve']:
            return [IsSecretaria() | IsAluno()]
        return [IsSecretaria()]

    @action(
    detail=True,
    methods=['post'],
    url_path='adicionar_relatorio'
)
    def adicionar_relatorio(self, request, pk=None):

        estagio = self.get_object()

        coordenador = Coordenador.objects.get(
            pk=request.data.get('coordenador')
        )

        relatorio = estagio.adicionar_relatorio(
            coordenador=coordenador,
            semestre=request.data.get('semestre'),
            horas_estagiadas=request.data.get('horas_estagiadas'),
            data_envio=request.data.get('data_envio')
        )

        serializer = RelatorioSemestralSerializer(relatorio)

        return Response(serializer.data, status=201)