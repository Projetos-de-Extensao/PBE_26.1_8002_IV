from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import validar_cpf, validar_cnpj

class Usuario(AbstractBaseUser):
    
    UNIDADE_CHOICES = [
    ('barra', 'Barra'),
    ('botafogo', 'Botafogo'),
    ]
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES)
    matricula = models.CharField(max_length=12, primary_key=True)
    senha = models.CharField(max_length=128)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
       return self.matricula

class Aluno(models.Model):
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula')
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])
    dt_nascimento = models.DateField()
    em_estagio = models.BooleanField(default=False)
    procurando_estagio = models.BooleanField(default=False)
    horas_estagio = models.IntegerField(default=0)
    periodo = models.PositiveIntegerField()

    def __str__(self):
        return self.usuario.nome
    
class Secretaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, db_column='matricula')

    def __str__(self):
        return self.usuario.nome

class Coordenador(models.Model):

    AREA_CHOICES = [
        ('negocios', 'Negócios'),
        ('tecnologia', 'Tecnologia'),
        ('financas', 'Finanças'),
        ('direito', 'Direito'),
        ('engenharia', 'Engenharia'),
    ]

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    area = models.CharField(max_length=100, choices=AREA_CHOICES)
    
    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        return self.usuario.nome

class Curso(models.Model):
    CURSOS_CHOICES = [
        ('administração', 'Administração'),
        ('análise e Desenvolvimento de Sistemas', 'Análise e desenvolvimento de sistemas'),
        ('Arquitetura e Urbanismo', 'Arquitetura e urbanismo'),
        ('ciência de dados e inteligência artificial', 'Ciência de Dados e Inteligência Artificial'),
        ('ciências Contábeis', 'Ciências contábeis'),
        ('direito', 'Direito'),
        ('ciências Econômicas', 'Ciências econômicas'),
        ('comunicação social - publicidade e propaganda', 'Comunicação Social - Publicidade e Propaganda'),
        ('engenharia civil', 'Engenharia Civil'),
        ('engenharia de produção', 'Engenharia de Produção'),
        ('engenharia da computação', 'Engenharia da Computação'),
        ('engenharia de software', 'Engenharia de Software'),
        ('relações internacionais', 'Relações Internacionais'),
    ]
    nome = models.CharField(max_length=100, choices=CURSOS_CHOICES, unique=True)

    def __str__(self):
        return self.nome

class Empresa(models.Model):

    nome = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    log = models.CharField(max_length=255, verbose_name="Logradouro")
    comp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Complemento")
    num = models.CharField(max_length=20, verbose_name="Número")
    bairro = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, primary_key=True, validators=[validar_cnpj])

    def __str__(self):
        return self.nome
    
class Tce(models.Model):
    anpoliceseguro = models.CharField(max_length=50, primary_key=True)
    bolsa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT, db_column='matricula_secretaria')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='matricula_aluno')

    def __str__(self):
        return self.anpoliceseguro
    
class Estagio(models.Model):
    idestagio = models.AutoField(primary_key=True)
    dtinicio = models.DateField()
    dtfim = models.DateField(null=True, blank=True)
    cargahorariasemanal = models.IntegerField()
    tce = models.ForeignKey(Tce, on_delete=models.PROTECT, db_column='n_apolice_seguro')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, db_column='cnpj')

    def __str__(self):
        return self.empresa.nome

class StatusRelatorio(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'

class RelatorioSemestral(models.Model):
    status = models.CharField(max_length=20, choices=StatusRelatorio.choices, default=StatusRelatorio.PENDENTE)
    idrelatorio = models.AutoField(primary_key=True)
    dataenvio = models.DateField()
    semestre = models.CharField(max_length=4, validators=[RegexValidator(regex=r'^\d{2}\.[12]$', message='O semestre deve estar no formato 26.1 ou 26.2')])
    horasestagio = models.PositiveIntegerField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='matricula')
    estagio = models.ForeignKey(Estagio, on_delete=models.CASCADE, db_column='id_estagio')

    def __str__(self):
        return self.status