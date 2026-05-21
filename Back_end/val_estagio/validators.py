from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

def validar_cpf(value):
    cpf = CPF()

    if not cpf.validate(value):
        raise ValidationError('CPF inválido')
    
    
"""
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
"""


def validar_cnpj(value):
    cnpj = CNPJ()

    if not cnpj.validate(value):
        raise ValidationError('CNPJ inválido')
    
def validar_matricula(x):
    if len(x) != 12:
        raise ValidationError('A Matrícula tem que ter 12 números.')   
    if not x.isdigit():
        raise ValidationError('A Matrícula so pode ter números.') 
    if not x.startswith('20'):
        raise ValidationError('A Matrícula deve começar com 20')   
   