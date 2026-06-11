from django.db import models

# O TextChoices é uma forma moderna e recomendada pelo Django de criar enumeradores (enums) para campos de escolha.
class StatusDocumento(models.TextChoices):
    # O primeiro valor é o que é salvo no banco, o segundo é o rótulo visível
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'

# Listas de tuplas para uso em campos 'choices' de modelos 
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