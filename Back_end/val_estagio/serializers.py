from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio
import django_filters.rest_framework

# --- SERIALIZADOR DE USUÁRIO ---

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador responsável por representar os dados básicos do usuário.
    Utilizado para expor informações da classe Usuario na API.
    """

    class Meta:
        model = Usuario
        fields = 'username', 'email', 'first_name', 'last_name', 'unidade', 'matricula'


# --- SERIALIZADOR DE CURSO ---

class CursoSerializer(serializers.ModelSerializer):
    """
    Serializador da entidade Curso.
    O identificador é somente leitura para evitar alterações indevidas.
    """

    class Meta:
        model = Curso
        fields = 'id', 'nome'
        read_only_fields = ['id']


# --- SERIALIZADOR DE ALUNO ---

class AlunoSerializer(serializers.ModelSerializer):

    # Recebe o ID do curso para criação/atualização do aluno
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(),
        source='curso'
    )

    # Exibe os dados completos do curso associado
    curso_nome = serializers.CharField(
    source='curso.nome',
    read_only=True
    )

    usuario_nome = serializers.CharField(
    source='usuario.username',
    read_only=True
    )

    # Exibe a matrícula proveniente do usuário vinculado
    matricula = serializers.CharField(
        source='usuario.matricula',
        read_only=True
    )

    class Meta:
        model = Aluno
        fields = (
            'usuario',
            'usuario_nome',
            'matricula',
            'telefone',
            'cpf',
            'dt_nascimento',
            'procurando_estagio',
            'horas_estagio',
            'periodo',
            'curso_nome',
            'curso_id'
        )

class AlunoSerializerPublico(serializers.ModelSerializer):
    """
    Versão restrita do AlunoSerializer.
    Usada quando o solicitante NÃO é Secretaria — omite dados sensíveis como CPF e telefone.
    """
    matricula = serializers.CharField(source='usuario.matricula', read_only=True)
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Aluno
        fields = (
            'usuario',
            'matricula',
            'periodo',
            'curso',
            'procurando_estagio',
        )

# --- SERIALIZADOR DE SECRETARIA ---

class SecretariaSerializer(serializers.ModelSerializer):

    # Exibe a matrícula do usuário associado à secretaria
    matricula_funcionario = serializers.CharField(
        source='usuario.matricula',
        read_only=True
    )

    class Meta:
        model = Secretaria
        fields = 'usuario', 'matricula_funcionario'


# --- SERIALIZADOR DE COORDENADOR ---

class CoordenadorSerializer(serializers.ModelSerializer):
    """
    Serializador responsável por representar os dados do coordenador.
    """

    class Meta:
        model = Coordenador
        fields = 'usuario', 'area'


# --- SERIALIZADOR DE EMPRESA ---

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = (
            'id',
            'nome',
            'telefone',
            'cnpj',
            'cep',
            'uf',
            'cidade',
            'log',
            'num',
            'comp',
            'bairro'
        )


# --- SERIALIZADOR DE TCE (TERMO DE COMPROMISSO DE ESTÁGIO) ---

class TceSerializer(serializers.ModelSerializer):

    # Recebe o aluno através de sua chave primária
    aluno_id = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(),
        source='aluno'
    )

    # Exibe o nome do aluno vinculado ao TCE
    aluno_nome = serializers.CharField(
        source='aluno.usuario.username',
        read_only=True
    )

    class Meta:
        model = Tce
        fields = "__all__"

        # O status é controlado pelas regras de negócio
        read_only_fields = ['status']


# --- SERIALIZADOR DE RELATÓRIO SEMESTRAL ---

class RelatorioSemestralSerializer(serializers.ModelSerializer):

    coordenador_id = serializers.PrimaryKeyRelatedField(
        queryset=Coordenador.objects.all(),
        source='coordenador'
    )

    coordenador_nome = serializers.CharField(
        source='coordenador.usuario.username',
        read_only=True
    )

    class Meta:
        model = RelatorioSemestral
        fields = (
            'idrelatorio',
            'semestre',
            'data_envio',
            'estagio',
            'horas_estagiadas',
            'coordenador_id',
            'coordenador_nome',
            'status'
        )

        read_only_fields = ['idrelatorio', 'status', 'estagio']


# --- SERIALIZADOR DE ESTÁGIO ----

class EstagioSerializer(serializers.ModelSerializer):

    # Recebe a empresa através de sua chave primária
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa'
    )

    # Exibe o nome da empresa vinculada ao estágio
    empresa_nome = serializers.CharField(
        source='empresa.nome',
        read_only=True
    )

    class Meta:
        model = Estagio
        fields = (
            'idestagio',
            'tce',
            'empresa_id',
            'empresa_nome',
            'dtinicio',
            'dtfim',
            'cargahorariasemanal'
        )

        # Identificador gerado automaticamente pelo banco
        read_only_fields = ['idestagio']

    # serializers.py — EstagioSerializer
    def validate(self, attrs):
        dtfim = attrs.get('dtfim')
        dtinicio = attrs.get('dtinicio')
        if dtfim and dtinicio and dtfim < dtinicio:
            raise serializers.ValidationError(
                {'dtfim': 'A data de término não pode ser anterior à data de início.'}
            )
        return attrs