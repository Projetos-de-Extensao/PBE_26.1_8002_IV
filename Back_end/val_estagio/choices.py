from django.db import models

class StatusDocumento(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'

UNIDADE_CHOICES = [
    ('barra', 'Barra'),
    ('botafogo', 'Botafogo'),
    ]

AREA_CHOICES = [
        ('negocios', 'Negócios'),
        ('tecnologia', 'Tecnologia'),
        ('financas', 'Finanças'),
        ('direito', 'Direito'),
        ('engenharia', 'Engenharia'),
    ]

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