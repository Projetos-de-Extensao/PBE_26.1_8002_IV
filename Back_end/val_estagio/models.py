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
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"    

    def __str__(self):
        return self.nome
