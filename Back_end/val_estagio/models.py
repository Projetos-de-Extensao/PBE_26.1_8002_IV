from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import validar_cpf, validar_cnpj

def cpf_valido(cpf):
    cpf = cpf.strip().replace('.','').replace('-','')
    multiplos = list(range(10, 1,-1))
    multiplos2 = list(range(11,1,-1))
        
    if not cpf.isnumeric() or len(cpf) != 11 or len(set(cpf)) == 1:
        raise ValidationError('CPF inválido. Verifique os números digitados.')
        
    soma_mult = sum(i * int(d) for i, d in zip(multiplos,cpf[0:9]))
        
    if soma_mult % 11 < 2 and int(cpf[9]) != 0:
        raise ValidationError('CPF inválido. Verifique os números digitados.')
    elif soma_mult % 11 > 1 and 11 - (soma_mult % 11) != int(cpf[9]):
        raise ValidationError('CPF inválido. Verifique os números digitados.')
        
    soma_mult2 = sum(i * int(d) for i, d in zip(multiplos2,cpf[0:10]))
        
    if soma_mult2 % 11 < 2 and int(cpf[10]) != 0:
        raise ValidationError('CPF inválido. Verifique os números digitados.')
    elif soma_mult2 % 11 > 1 and 11 - (soma_mult2 % 11) != int(cpf[10]):
        raise ValidationError('CPF inválido. Verifique os números digitados.')

class Usuario(AbstractUser):
    
    UNIDADE_CHOICES = [
    ('barra', 'Barra'),
    ('botafogo', 'Botafogo'),
    ]
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES)
    
    def __str__(self):
       return self.username 

class Aluno(models.Model):
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=12, unique=True)
    cpf = models.CharField(max_length=14, unique=True, validators=[cpf_valido])
    dt_nascimento = models.DateField()
    procurando_estagio = models.BooleanField(default=True)
    horas_estagio = models.IntegerField(default=0)
    periodo = models.PositiveIntegerField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula
    
class Secretaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula_funcionario = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.matricula_funcionario
    
    
class Coordenador(models.Model):

    AREA_CHOICES = [
        ('negocios', 'Negócios'),
        ('tecnologia', 'Tecnologia'),
        ('financas', 'Finanças'),
        ('direito', 'Direito'),
        ('engenharia', 'Engenharia'),
    ]

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    area = models.CharField(max_length=20, choices=AREA_CHOICES)
    cursos = models.ManyToManyField('Curso', blank=True)
    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        return self.usuario.username

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

    nome_empresa = models.CharField(max_length=100, verbose_name="Nome da Empresa")
    endereco_empresa = models.CharField(max_length=180, verbose_name= "Endereço da Empresa")
    cnpj = models.CharField(max_length=18, unique=True, validators=[validar_cnpj])

    def __str__(self):
        return self.nome_empresa
    
class Seguradora(models.Model):
    apolice_seguro = models.PositiveIntegerField(verbose_name="Apolice de Seguro", unique=True)
    nome_seguradora = models.CharField(max_length=100, verbose_name="Nome da Seguradora")

    def __str__(self):
        return self.nome_seguradora

class StatusRelatorio(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'

class RelatorioSemestral(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    estagio = models.ForeignKey('Estagio', on_delete=models.CASCADE)
    horas_estagiadas = models.PositiveIntegerField()
    em_aberto = models.BooleanField(default=True)
    semestre = models.CharField(max_length=4, validators=[RegexValidator(regex=r'^\d{2}\.[12]$', message='O semestre deve estar no formato 26.1 ou 26.2')])
    data_envio = models.DateField(verbose_name="Data de envio")
    status = models.CharField(max_length=20, choices=StatusRelatorio.choices, default=StatusRelatorio.PENDENTE)

    def __str__(self):
        return self.status
    
class Tce(models.Model):
    auxilio_bolsa = models.DecimalField(max_digits=8, decimal_places=2)
    seguradora = models.ForeignKey('Seguradora', on_delete=models.CASCADE)
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    empresa_contratante = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name="Empresa Contratante")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_fim = models.DateField(verbose_name="Data de fim")
    status = models.CharField(max_length=20, choices=StatusRelatorio.choices)

    def __str__(self):
        return self.empresa_contratante.nome_empresa
    
class Estagio(models.Model):
    tce = models.OneToOneField('Tce', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_fim = models.DateField(verbose_name="Data de fim")
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.empresa.nome_empresa
    






    # area
    # cursos que coordena
    #pass#

    #def receber_relatorios(self):#
        # lógica para receber os relatórios#
        #pass#

    #def validar_relatorio(self, relatorio, aluno):#
        # lógica para validar os relatórios#
       # pass#


