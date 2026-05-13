from django.db import models

class Usuario(models.Model):
    
    UNIDADE_CHOICES = [
    ('barra', 'Barra'),
    ('botafogo', 'Botafogo'),
    ]
    nome = models.CharField(max_length=50) 
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10)
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES)
    
    class Meta:
        abstract = True

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"    

    def __str__(self):
        return self.nome

class Aluno(Usuario):
    
    matricula = models.CharField(max_length=12, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    dt_nascimento = models.DateField()
    em_estagio = models.BooleanField(default=False)
    procurando_estagio = models.BooleanField(default=True)
    horas_estagio = models.IntegerField(default=0)
    periodo = models.IntegerField(max_length=1)
    #TCE
    #trabalho
    #curso
    

class Secretaria(Usuario):
    matricula_funcionario = models.CharField(max_length=12, unique=True)
    
class Coordenador(Usuario):
    # area
    # cursos que coordena
    pass


"""
Cursos da Ibmec para a futura classe Curso
CURSOS_CHOICES = [
        ('Administração', 'administração'),
        ('Análise e Desenvolvimento de Sistemas', 'análise e desenvolvimento de sistemas'),
        ('Arquitetura e Urbanismo', 'arquitetura e urbanismo'),
        ('Ciência de Dados e Inteligência Artificial', 'ciência de dados e inteligência artificial'),
        ('Ciências Contábeis', 'ciências contábeis'),
        ('Direito', 'direito'),
        ('Ciências Econômicas', 'ciências econômicas'),
        ('Comunicação Social - Publicidade e Propaganda', 'comunicação social - publicidade e propagando'),
        ('Engenharia Civil', 'engenharia civil'),
        ('Engenharia de Produção', 'engenharia de produção'),
        ('Engenharia da Computação', 'engenharia da computação'),
        ('Engenharia de Software', 'engenharia de software'),
        ('Relações Internacionais', 'relações internacionais'),
    ]"""