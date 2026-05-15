from django.db import models
from django.contrib.auth.models import AbstractUser

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
    cpf = models.CharField(max_length=11, unique=True)
    dt_nascimento = models.DateField()
    em_estagio = models.BooleanField(default=False)
    procurando_estagio = models.BooleanField(default=True)
    horas_estagio = models.IntegerField(default=0)
    periodo = models.PositiveIntegerField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula
    
    #TCE
    #trabalho
    #curso
    
    #def esta_disponivel(self):#
        #return not self.em_estagio and self.procurando_estagio#
    
   # def ganhar_horas_estagio(self, horas):
        #if type(horas) == int and int(horas) > 0:#
         #    self.horas_estagio += int(horas) #
         # self.save()#
    #def enviar_relatorio(self, relatorio):#
        # lógica para enviar o relatório#
        #pass#
    
    #def abrir_chamado(self, documentos):#
        # lógica para abrir um chamado
        #pass#
        
    
class Secretaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula_funcionario = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.matricula_funcionario

    
    #def assinar_tce(self, tce):#
        # lógica para assinar o TCE
        #pass#
    
    
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





    # area
    # cursos que coordena
    #pass#

    #def receber_relatorios(self):#
        # lógica para receber os relatórios#
        #pass#

    #def validar_relatorio(self, relatorio, aluno):#
        # lógica para validar os relatórios#
       # pass#


