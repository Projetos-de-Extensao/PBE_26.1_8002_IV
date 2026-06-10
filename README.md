# Sistema de Validação de Estágios

Projeto desenvolvido na disciplina **IBM8936 - Projeto Back-End**, utilizando Django e Django REST Framework para gerenciamento e validação de processos de estágio.

---

## Sobre o Projeto

O Sistema de Validação de Estágios tem como objetivo auxiliar no gerenciamento do fluxo acadêmico de estágios, permitindo o controle de alunos, empresas, termos de compromisso, relatórios semestrais e contabilização das horas obrigatórias de estágio.

Durante o desenvolvimento foram aplicados conceitos de:

- Programação Orientada a Objetos (POO)
- Desenvolvimento de APIs REST
- Modelagem de Banco de Dados
- Versionamento com Git e GitHub
- Boas Práticas de Desenvolvimento
- Documentação de Software
- Segurança e Validação de Dados

---

## Tecnologias Utilizadas

- Python 3.14
- Django 6.0
- Django REST Framework
- SQLite3
- Django Filter
- DRF Spectacular (Swagger/OpenAPI)
- MkDocs
- Git e GitHub

---

## Funcionalidades

### Alunos

- Cadastro de alunos
- Controle de horas de estágio
- Associação a cursos

### Empresas

- Cadastro de empresas concedentes
- Validação de CNPJ
- Controle de informações de contato

### TCE (Termo de Compromisso de Estágio)

- Cadastro de TCE
- Aprovação por secretaria
- Reprovação por secretaria
- Controle de status

### Relatórios Semestrais

- Cadastro de relatórios
- Aprovação por coordenador
- Reprovação por coordenador
- Atualização automática das horas do aluno

### API

- CRUD completo para todas as entidades
- Paginação
- Filtros
- Documentação automática com Swagger
- Endpoints customizados para aprovação e reprovação

---

## Estrutura do Projeto

```text
PBE_26.1_8002_IV/
│
├── Back_end/
│   ├── Back_end/
│   ├── val_estagio/
│   ├── manage.py
│
├── docs/
│
├── .env.example
├── requirements.txt
├── iniciar.py
├── mkdocs.yml
└── README.md
```

---

## Instalação

### 1. Clonar o Repositório

```bash
git clone <https://github.com/Projetos-de-Extensao/PBE_26.1_8002_IV.git>
cd PBE_26.1_8002_IV
```

### 2. Criar Ambiente Virtual

```bash
python -m venv .venv
```

### 3. Ativar Ambiente Virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## Configuração do Ambiente

Crie um arquivo `.env` utilizando como base o arquivo `.env.example`.

Exemplo:

```env
SECRET_KEY=sua_secret_key
FIELD_ENCRYPTION_KEY=sua_chave_de_criptografia
DEBUG=True
CORS_ALLOW_ORIGINS=http://localhost:3000
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Inicialização Automática

O projeto possui um script de inicialização responsável por:

- Instalar dependências
- Verificar alterações nos models
- Executar migrations
- Inicializar o servidor Django

Execute:

```bash
python iniciar.py
```

Após a inicialização, a API estará disponível em:

```text
http://127.0.0.1:8000/
```

---

## Inicialização Manual

Caso deseje executar os comandos individualmente:

### Criar Migrations

```bash
python manage.py makemigrations
```

### Aplicar Migrations

```bash
python manage.py migrate
```

### Executar Servidor

```bash
python manage.py runserver
```

---

## Documentação da API

### Swagger UI

```text
http://127.0.0.1:8000/api/docs/
```

### Redoc

```text
http://127.0.0.1:8000/api/redoc/
```

### Schema OpenAPI

```text
http://127.0.0.1:8000/api/schema/
```

---

## Filtros Disponíveis

### TCE

```http
GET /api/tces/?status=aprovado
GET /api/tces/?aluno=202500000001
```

### Relatórios

```http
GET /api/relatorios/?status=aprovado
GET /api/relatorios/?semestre=26.1
```

---

## Testes

Para executar os testes automatizados:

```bash
python manage.py test
```

Os testes cobrem:

- Criação de TCE
- Fluxo de aprovação de TCE
- Reprovação de relatório
- Atualização de horas de estágio do aluno

---

## Segurança

O sistema implementa:

- Validação de CPF
- Validação de CNPJ
- Validação de CEP
- Criptografia de dados sensíveis
- Rate Limiting (Throttling)
- Variáveis sensíveis armazenadas em arquivo `.env`

---

## Integrantes da Equipe

| Nome |
|--------|
| Rafael Correa |
| Heitor Lima |
| Bernardo Fontes |
| Caio Salomão |
| Carlos Vinícius |

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina Projeto Back-End (IBM8936).
