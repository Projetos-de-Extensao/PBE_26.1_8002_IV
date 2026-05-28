from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'username', 'email', 'first_name', 'last_name', 'unidade', 'matricula'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = 'id', 'nome'
        read_only_fields = ['id']

class AlunoSerializer(serializers.ModelSerializer):
    curso_id = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all(),source='curso')
    curso = CursoSerializer(read_only=True)
    matricula = serializers.CharField(
        source='usuario.matricula',
        read_only=True
    )

    class Meta:
        model = Aluno
        fields = 'usuario', 'matricula', 'telefone', 'cpf', 'dt_nascimento', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso', 'curso_id'

class SecretariaSerializer(serializers.ModelSerializer):
    matricula_funcionario = serializers.CharField(
        source='usuario.matricula',
        read_only=True
    )
    
    class Meta:
        model = Secretaria
        fields ='usuario','matricula_funcionario'

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields ='usuario', 'area'

class EmpresaSerializer(serializers.ModelSerializer):
    nome_empresa = serializers.CharField(source='nome', read_only=True)
    class Meta:
        model = Empresa
        fields ='nome_empresa', 'telefone', 'cnpj', 'cep', 'uf', 'cidade', 'log', 'num', 'comp', 'bairro' 


class TceSerializer(serializers.ModelSerializer):
    aluno_id = serializers.PrimaryKeyRelatedField(queryset = Aluno.objects.all(), source='aluno')
    aluno_nome = serializers.CharField(source='aluno.usuario.username', read_only=True)

    class Meta:
        model = Tce
        fields ='bolsa', 'apoliceseguro', 'secretaria','aluno_id', 'aluno_nome', 'status'
        read_only_fields = ['status']

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    
    coordenador_nome = serializers.CharField(source='coordenador.usuario.username', read_only=True)

    class Meta:
        model = RelatorioSemestral
        fields = 'idrelatorio', 'semestre', 'data_envio', 'estagio', 'horas_estagiadas', 'coordenador_nome', 'status'
        read_only_fields = ['idrelatorio', 'status']

class EstagioSerializer(serializers.ModelSerializer):
    empresa_id = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all(),source='empresa')
    empresa_nome = serializers.CharField(source='empresa.nome', read_only=True)

    class Meta:
        model = Estagio
        fields = 'idestagio', 'tce', 'empresa_id', 'empresa_nome', 'dtinicio', 'dtfim', 'cargahorariasemanal'
        read_only_fields = ['idestagio']