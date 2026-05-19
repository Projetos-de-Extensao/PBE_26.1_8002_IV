legendas:

Negrito = PK
Italico = FK

usuario(**matricula**, senha, nome, email)

secretaria(***matricula***)

aluno(***matricula***, cpf, dtnascimento, emestagio, procurandoestagio, horaestagio, periodo, *napoliceseguro*)

coordenador(***matricula***, area)

curso(**idcurso**, nomecurso, *matricula*)

tce(**anpoliceseguro**, bolsa)

assina(***matricula***, ***anpoliceseguro***)

estagio(**idestagio**, dtinicio, dtfim, cargahorariasemanal, *napoliceseguro* *cnpj*)

empresa(**cnpj**, nome, cep, uf, cidade, log, comp, num, bairro)

relatoriosemestral(**idrelatorio**, dataenvio, semestre, horasestagio, *matricula*, *idestagio*)