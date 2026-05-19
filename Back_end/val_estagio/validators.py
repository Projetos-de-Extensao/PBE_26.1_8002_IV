from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

def validar_cpf(value):
    cpf = CPF()

    if not cpf.validate(value):
        raise ValidationError('CPF inválido')

def validar_cnpj(value):
    cnpj = CNPJ()

    if not cnpj.validate(value):
        raise ValidationError('CNPJ inválido')