# Requisitos do projeto

## Stakeholders

- Estudantes: Pessoas que utilizam o software para dar entrada no processo
- Secretaria: Responsável por validar e acompanhar os estágios dos alunos.
- Cordenador: Aprovar/Reprovar relatório semestral/ Avaliar horas estagiadas enviadas pelo aluno


## Requisitos

### Funcionais

| Id | Requisito | Prioridade|
|----|-----------|-----------|
|RF01|O aluno deve ser capaz de se logar|Alto|
|RF03|O aluno deve ser capaz de enviar a documentação|Alto|
|RF04|O aluno deve ser capaz de acompanhar o status do seu chamado|Médio|
|RF05|O aluno deve editar seus dados cadastrais|Médio|
|RF06|A secretaria deve aprovar ou reprovar o estágio|Alto|
|RF07|A secretaria deve ter acesso aos perfis dos alunos com informações|Alto|
|RF08|A secretaria deve visualizar todos os chamados abertos|Alto|
|RF09|A secretaria deve atualizar o status dos chamados|Alto|
|RF10|A secretaria deve buscar alunos pelo nome ou matrícula|Alto|

### Não-Funcionais

- **Segurança:** O sistema deve proteger dados sensíveis seguindo a LGPD dos alunos e das empresas
- **Responsividade:** O sistema deve ser responsivo para navegadores modernos (Chrome, Firefox, Brave, etc) e dispositivos(laptops, desktops, celulares e tablets)
- **Confiabilidade:** O sistema deve garantir que os dados não sejam perdidos em caso de falhas.
- **Manutenibilidade:** O código do sistema deve ser organizado e documentado para facilitar futuras manutenções.
- **Escalabilidade:** O sistema deve suportar o aumento do número de usuários sem degradação significativa de desempenho.
-**Usabilidade** O sistema deve ter uma arquitetura intuitiva para os usuários

### Matriz de Rastreabilidade
| Requisito                                                                 | ViewSet(s)                                                                                    | Serializer(s)                                   | Status       |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------ |
| RF01 – O aluno deve ser capaz de se logar                                 |                                                                                               |                                                 | Parcial      |
| RF03 – O aluno deve ser capaz de enviar a documentação                    | `TceViewSet.create`, `EstagioViewSet.adicionar_relatorio`, `RelatorioSemestralViewSet.create` | `TceSerializer`, `RelatorioSemestralSerializer` | Implementado |
| RF04 – O aluno deve ser capaz de acompanhar o status do seu chamado       | `TceViewSet.retrieve/list`, `RelatorioSemestralViewSet.retrieve/list`                         | `TceSerializer`, `RelatorioSemestralSerializer` | Implementado |
| RF05 – O aluno deve editar seus dados cadastrais                          | `AlunoViewSet.update`, `AlunoViewSet.partial_update`                                          | `AlunoSerializer`                               | Implementado |
| RF06 – A secretaria deve aprovar ou reprovar o estágio                    | `TceViewSet.aprovar_tce`, `TceViewSet.reprovar_tce`                                           | `TceSerializer`                                 | Implementado |
| RF07 – A secretaria deve ter acesso aos perfis dos alunos com informações | `AlunoViewSet.list`, `AlunoViewSet.retrieve`                                                  | `AlunoSerializer`                               | Implementado |
| RF08 – A secretaria deve visualizar todos os chamados abertos             | `TceViewSet.list`, `RelatorioSemestralViewSet.list`, filtros por status                       | `TceSerializer`, `RelatorioSemestralSerializer` | Implementado |
| RF09 – A secretaria deve atualizar o status dos chamados                  | `TceViewSet.aprovar_tce`, `TceViewSet.reprovar_tce`                                           | `TceSerializer`                                 | Implementado |
| RF10 – A secretaria deve buscar alunos pelo nome ou matrícula             | `AlunoViewSet` (`search_fields`)                                                              | `AlunoSerializer`                               | Implementado |