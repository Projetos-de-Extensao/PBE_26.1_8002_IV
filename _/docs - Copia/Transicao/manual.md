# Manual do Usuário

## Introdução

O Sistema de Validação de Estágios foi desenvolvido para auxiliar no gerenciamento dos processos de estágio dos alunos, permitindo o cadastro e acompanhamento de empresas, TCEs, estágios e relatórios semestrais.

---

## Perfis do Sistema

### Aluno

O aluno pode:

- Visualizar seus dados cadastrais.
- Consultar seus TCEs.
- Consultar seus estágios.
- Acompanhar seus relatórios semestrais.
- Verificar a quantidade de horas de estágio acumuladas.

### Secretaria

A secretaria pode:

- Gerenciar alunos.
- Gerenciar empresas.
- Aprovar ou reprovar TCEs.
- Consultar informações do sistema.

### Coordenador

O coordenador pode:

- Consultar relatórios semestrais.
- Aprovar relatórios.
- Reprovar relatórios.

---

## Como acessar o sistema

1. Abra a aplicação.
2. Informe seu usuário e senha.
3. Clique em **Entrar**.

---

## Fluxo de Utilização

### Cadastro de Empresa

1. Acesse o módulo **Empresas**.
2. Clique em **Novo Cadastro**.
3. Preencha os dados da empresa.
4. Clique em **Salvar**.

### Cadastro de TCE

1. Acesse o módulo **TCE**.
2. Clique em **Novo TCE**.
3. Informe os dados solicitados.
4. Clique em **Salvar**.

### Aprovação de TCE

1. Acesse a lista de TCEs.
2. Selecione o TCE desejado.
3. Clique em **Aprovar** ou **Reprovar**.

### Cadastro de Estágio

1. Acesse o módulo **Estágios**.
2. Clique em **Novo Estágio**.
3. Associe o estágio a um TCE aprovado.
4. Informe a empresa e os dados do estágio.
5. Clique em **Salvar**.

### Cadastro de Relatório Semestral

1. Acesse o estágio desejado.
2. Clique em **Adicionar Relatório**.
3. Informe:
   - Semestre
   - Data de envio
   - Horas estagiadas
4. Clique em **Salvar**.

### Aprovação de Relatório

1. Acesse a lista de relatórios.
2. Selecione o relatório desejado.
3. Clique em **Aprovar** ou **Reprovar**.

Ao aprovar um relatório, as horas de estágio são adicionadas automaticamente ao aluno.

---

## Regras do Sistema

- O limite máximo de horas contabilizadas é de **350 horas**.
- CPF e CNPJ são validados pelo sistema.
- Um relatório aprovado não gera horas duplicadas.
- Não é permitido cadastrar relatórios duplicados para o mesmo semestre e estágio.
- Não é permitido cadastrar estágios com data de término anterior à data de início.

---

## Documentação da API

A documentação da API pode ser acessada através do Swagger/OpenAPI disponibilizado pelo sistema.

---

## Suporte

Em caso de dúvidas, consulte a documentação do projeto ou entre em contato com a equipe responsável pelo desenvolvimento.