legendas:

Negrito = PK
Italico = FK

usuario(**matricula**, senha, nome, email)

secretaria(***matricula***)

aluno(***matricula***, cpf, dtnascimento, emestagio, procurandoestagio, horaestagio, periodo)

coordenador(***matricula***, area)

curso(**idcurso**, nomecurso, *matricula*)

tce(**anpoliceseguro**, bolsa, *matriculasecretaria*, *matriculaaluno*)

estagio(**idestagio**, dtinicio, dtfim, cargahorariasemanal, *napoliceseguro* *cnpj*)

empresa(**cnpj**, nome, cep, uf, cidade, log, comp, num, bairro)

relatoriosemestral(**idrelatorio**, dataenvio, semestre, horasestagio, *matricula*, *idestagio*)