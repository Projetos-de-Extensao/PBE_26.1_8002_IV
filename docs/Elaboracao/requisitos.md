# Requisitos do projeto

## Stakeholders

- Estudantes: Pessoas que utilizam o software para dar entrada no processo
- Secretaria: Responsável por validar e acompanhar os estágios dos alunos.
- Cordenador: Aprovar/Reprovar relatório semestral/ Avaliar horas estagiadas enviadas pelo aluno


## Requisitos

### Funcionais

## Requisitos Funcionais

| Id   | Requisito                                                              | Prioridade |
| ---- | ---------------------------------------------------------------------- | ---------- |
| RF01 | O usuário deve ser capaz de se autenticar no sistema                   | Alto       |
| RF02 | O aluno deve visualizar seus dados cadastrais                          | Alto       |
| RF03 | A secretaria deve cadastrar e gerenciar empresas                       | Alto       |
| RF04 | O aluno deve cadastrar Termos de Compromisso de Estágio (TCE)          | Alto       |
| RF05 | A secretaria deve aprovar ou reprovar TCEs                             | Alto       |
| RF06 | A secretaria deve cadastrar estágios vinculados a TCEs aprovados       | Alto       |
| RF07 | O aluno deve enviar relatórios semestrais de estágio                   | Alto       |
| RF08 | O coordenador deve aprovar ou reprovar relatórios semestrais           | Alto       |
| RF09 | O sistema deve controlar automaticamente as horas de estágio do aluno  | Alto       |
| RF10 | A secretaria e o coordenador devem buscar alunos por nome ou matrícula | Alto       |


### Não-Funcionais

- **Segurança:** O sistema deve proteger dados sensíveis seguindo a LGPD dos alunos e das empresas
- **Responsividade:** O sistema deve ser responsivo para navegadores modernos (Chrome, Firefox, Brave, etc) e dispositivos(laptops, desktops, celulares e tablets)
- **Confiabilidade:** O sistema deve garantir que os dados não sejam perdidos em caso de falhas.
- **Manutenibilidade:** O código do sistema deve ser organizado e documentado para facilitar futuras manutenções.
- **Escalabilidade:** O sistema deve suportar o aumento do número de usuários sem degradação significativa de desempenho.
-**Usabilidade** O sistema deve ter uma arquitetura intuitiva para os usuários

### Matriz de Rastreabilidade
| Requisito | Implementação | Status |
|------------|------------|------------|
| RF01 – Autenticação | CustomAuthToken | Implementado |
| RF02 – Visualização de dados do aluno | AlunoViewSet | Implementado |
| RF03 – Cadastro de TCE | TceViewSet.create | Implementado |
| RF04 – Consulta de status | TceViewSet e RelatorioSemestralViewSet | Implementado |
| RF05 – Edição de dados do aluno | AlunoViewSet.update | Implementado |
| RF06 – Aprovação/Reprovação de TCE | aprovar_tce / reprovar_tce | Implementado |
| RF07 – Consulta de alunos | AlunoViewSet.list / retrieve | Implementado |
| RF08 – Aprovação/Reprovação de Relatórios | aprovar_relatorio / reprovar_relatorio | Implementado |
| RF09 – Controle de horas | ganhar_horas_estagio() | Implementado |
| RF10 – Busca de alunos | SearchFilter | Implementado |