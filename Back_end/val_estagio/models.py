from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validar_cpf, validar_cnpj, validar_matricula, validar_cep, validar_periodo, validar_positivo


class StatusDocumento(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'


class Usuario(AbstractUser):
    
    UNIDADE_CHOICES = [
    ('barra', 'Barra'),
    ('botafogo', 'Botafogo'),
    ]
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, verbose_name="Unidade")
    matricula = models.CharField(max_length=12, primary_key=True, verbose_name="Matrícula", validators=[validar_matricula])
    
    def __str__(self):
       return self.matricula

class Aluno(models.Model):
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula', verbose_name="Matrícula")
    telefone = PhoneNumberField(region='BR', verbose_name="Telefone")
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf], verbose_name="CPF")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")
    procurando_estagio = models.BooleanField(default=False, verbose_name="Procurando Estágio")
    horas_estagio = models.IntegerField(default=0, verbose_name="Horas de Estágio")
    periodo = models.PositiveIntegerField(verbose_name="Período", validators=[validar_periodo])
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, db_column='id_curso', verbose_name="Curso")
    
    def ganhar_horas_estagio(self, horas_estagiadas):
        if(horas_estagiadas > 0 and self.horas_estagio < 350):
            self.horas_estagio = min(self.horas_estagio + horas_estagiadas, 350)
        self.save()

    def __str__(self):
        return self.usuario.username
    
class Secretaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula')

    def aprovar_tce(self, tce):
        tce.se_aprovar()

    def reprovar_tce(self, tce):
        tce.se_reprovar()

    def __str__(self):
        return self.usuario.username

class Coordenador(models.Model):

    AREA_CHOICES = [
        ('negocios', 'Negócios'),
        ('tecnologia', 'Tecnologia'),
        ('financas', 'Finanças'),
        ('direito', 'Direito'),
        ('engenharia', 'Engenharia'),
    ]

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    area = models.CharField(max_length=100, choices=AREA_CHOICES, verbose_name="Área")

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def aprovar_relatorio(self, RelatorioSemestral):
        RelatorioSemestral.se_aprovar()

    def reprovar_relatorio(self, RelatorioSemestral):
        RelatorioSemestral.se_reprovar()

    def __str__(self):
        return self.usuario.username

class Curso(models.Model):
    CURSOS_CHOICES = [
        ('administração', 'Administração'),
        ('analise e desenvolvimento de sistemas', 'Análise e Desenvolvimento de Sistemas'),
        ('arquitetura e urbanismo', 'Arquitetura e Urbanismo'),
        ('ciencia de dados e inteligencia artificial', 'Ciência de Dados e Inteligência Artificial'),
        ('ciencias contabeis', 'Ciências Contábeis'),
        ('direito', 'Direito'),
        ('ciencias economicas', 'Ciências Econômicas'),
        ('comunicacao social - publicidade e propaganda', 'Comunicação Social - Publicidade e Propaganda'),
        ('engenharia civil', 'Engenharia Civil'),
        ('engenharia de producao', 'Engenharia de Produção'),
        ('engenharia da computacao', 'Engenharia da Computação'),
        ('engenharia de software', 'Engenharia de Software'),
        ('relacoes internacionais', 'Relações Internacionais'),
    ]
    nome = models.CharField(max_length=100, choices=CURSOS_CHOICES, unique=True, verbose_name="Nome do Curso")

    def __str__(self):
        return self.nome

class Empresa(models.Model):

    nome = models.CharField(max_length=255, verbose_name="Nome da Empresa")
    telefone = PhoneNumberField(region='BR', verbose_name="Telefone")
    cep = models.CharField(max_length=9, verbose_name="CEP", validators=[validar_cep])
    uf = models.CharField(max_length=2, verbose_name="UF")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    log = models.CharField(max_length=255, verbose_name="Logradouro")
    comp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Complemento")
    num = models.CharField(max_length=20, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cnpj = models.CharField(max_length=18, primary_key=True, validators=[validar_cnpj], verbose_name="CNPJ")

    def __str__(self):
        return self.nome
    
class Tce(models.Model):
    status = models.CharField(max_length=20, choices=StatusDocumento.choices, default=StatusDocumento.PENDENTE, verbose_name="Status do TCE")
    apoliceseguro = models.CharField(max_length=50, primary_key=True, verbose_name="Apólice de Seguro",)
    bolsa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Bolsa", validators=[validar_positivo])
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT, db_column='matricula_secretaria', verbose_name="Secretaria")
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='matricula_aluno', verbose_name="Aluno")

    def se_aprovar(self):
        self.status = StatusDocumento.APROVADO
        self.save()

    def se_reprovar(self):
        self.status = StatusDocumento.REPROVADO
        self.save()
    

    def __str__(self):
        return self.apoliceseguro
    
class Estagio(models.Model):
    idestagio = models.AutoField(primary_key=True)
    dtinicio = models.DateField(verbose_name="Data de Início")
    dtfim = models.DateField(null=True, blank=True, verbose_name="Data de Término")
    cargahorariasemanal = models.IntegerField(verbose_name="Carga Horária Semanal")
    tce = models.ForeignKey(Tce, on_delete=models.PROTECT, db_column='apolice_seguro', verbose_name="TCE")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, db_column='cnpj', verbose_name="Empresa")

    def __str__(self):
        return self.empresa.nome


class RelatorioSemestral(models.Model):
    status = models.CharField(max_length=20, choices=StatusDocumento.choices, default=StatusDocumento.PENDENTE, verbose_name="Status do Relatório")
    idrelatorio = models.AutoField(primary_key=True)
    data_envio = models.DateField(verbose_name="Data de Envio")
    semestre = models.CharField(max_length=4, validators=[RegexValidator(regex=r'^\d{2}\.[12]$', message='O semestre deve estar no formato 26.1 ou 26.2')], verbose_name="Semestre")
    horas_estagiadas = models.PositiveIntegerField(verbose_name="Horas Estagiadas", validators=[validar_positivo])
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, db_column='matricula_coordenador', verbose_name="Coordenador")
    estagio = models.ForeignKey(Estagio, on_delete=models.CASCADE, db_column='id_estagio', verbose_name="Estágio")

    def se_aprovar(self, Aluno):
        self.status = StatusDocumento.APROVADO
        Aluno.ganhar_horas_estagio(self.horas_estagiadas)
        self.save()

    def se_reprovar(self):
        self.status = StatusDocumento.REPROVADO
        self.save()

    class Meta:
        verbose_name = "Relatório Semestral"
        verbose_name_plural = "Relatórios Semestrais"
        unique_together = ['estagio', 'semestre']

    def __str__(self):
        return self.status