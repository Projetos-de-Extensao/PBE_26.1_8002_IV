from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ
from pycep_correios import get_address_from_cep
from requests.exceptions import ConnectionError, Timeout
import re


# --- VALIDADOR DE SEMESTRE ----

def validar_semestre(value):
    """
    Valida se o semestre está no formato:
    AA.1 ou AA.2

    Exemplos válidos:
    26.1
    26.2
    """

    if not re.fullmatch(r'\d{2}\.[12]', value):
        raise ValidationError(
            'O semestre deve estar no formato 26.1 ou 26.2'
        )


# --- VALIDADOR DE CPF ---

def validar_cpf(value):
    """
    Utiliza a biblioteca validate-docbr para verificar
    a autenticidade do CPF informado.
    """

    cpf = CPF()

    if not cpf.validate(value):
        raise ValidationError('CPF inválido')


"""
# --- IMPLEMENTAÇÃO MANUAL DE VALIDAÇÃO DE CPF ---

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


# --- VALIDADOR DE CNPJ ---

def validar_cnpj(value):
    """
    Utiliza a biblioteca validate-docbr para validar
    a autenticidade do CNPJ informado.
    """

    cnpj = CNPJ()

    if not cnpj.validate(value):
        raise ValidationError('CNPJ inválido')


# --- VALIDADOR DE MATRÍCULA ---

def validar_matricula(x):
    """
    Regras da matrícula:

    - Deve possuir exatamente 12 dígitos;
    - Deve conter apenas números;
    - Deve iniciar com "20".
    """

    if len(x) != 12:
        raise ValidationError('A Matrícula tem que ter 12 números.')

    if not x.isdigit():
        raise ValidationError('A Matrícula so pode ter números.')

    if not x.startswith('20'):
        raise ValidationError('A Matrícula deve começar com 20')


# --- VALIDADOR DE CEP ---

def validar_cep(x):
    """
    Valida a existência do CEP consultando
    o serviço dos Correios.

    Também trata possíveis indisponibilidades
    da API externa.
    """

    cep = x.replace('-', '')

    try:
        get_address_from_cep(cep)

    except (ConnectionError, Timeout):
        raise ValidationError(
            'Serviço de validação de CEP indisponível. Tente novamente mais tarde.'
        )

    except Exception as erro:
        raise ValidationError('CEP inválido') from erro


# --- VALIDADOR DE PERÍODO ---

def validar_periodo(x):
    """
    O período acadêmico deve estar entre
    o 1º e o 10º período.
    """

    if x < 1 or x > 10:
        raise ValidationError(
            'O Período tem que estar entre 1 e 10'
        )


# --- VALIDADOR DE VALORES POSITIVOS ---

def validar_positivo(x):
    """
    Garante que o valor informado
    não seja negativo.
    """

    if x < 0:
        raise ValidationError(
            'O Valor não pode ser negativo'
        )


"""
# --- IMPLEMENTAÇÃO MANUAL DE VALIDAÇÃO DE TELEFONE ---

def validar_telefone(value):

    if len(value) != 15:
        raise ValidationError(
            'Telefone deve estar no formato "(21) 99999-9999"'
        )

    if value[0] != '(':
        raise ValidationError('Falta "(" no DDD')

    if value[3] != ')':
        raise ValidationError('Falta ")" no DDD')

    if value[4] != ' ':
        raise ValidationError('Deve haver espaço após o DDD')

    if value[10] != '-':
        raise ValidationError('Falta "-" no telefone')

    numeros = value[1:3] + value[5:10] + value[11:]

    if not numeros.isdigit():
        raise ValidationError(
            'Telefone deve conter apenas números'
        )
"""