
/* ****************************** FATOS PARA O ESQUEMA CONCEITUAL ************************ */

eForte(empregado).
eForte(departamento).
eForte(projeto).
eFraca(dependente).

chaveDe(ssn, empregado).
chaveDe(numero, departamento).
chaveDe(numero, projeto).
chaveDe(nome, dependente).

atributoDe(nome, tipoSimples, empregado).
atributoDe(endereco, tipoSimples, empregado).
atributoDe(sexo, tipoSimples, empregado).
atributoDe(datanascimento, tipoSimples, empregado).
atributoDe(salario, tipoSimples, empregado).

atributoDe(nome, tipoSimples, departamento).
atributoDe(localizacao, tipoMultivalorado, departamento).
atributoDe(numEmpregado, tipoCalculado, departamento).

atributoDe(nome, tipoSimples, projeto).
atributoDe(localizacao, tipoSimples, projeto).

atributoDe(sexo, tipoSimples, dependente).
atributoDe(datanascimento, tipoSimples, dependente).
atributoDe(parentesco, tipoSimples, dependente).

atributoDe(dataInicio, tipoSimples, gerencia).

atributoDe(horas, tipoSimples, trabalhaEm).


relacionamento( dependentesDe,
		    componente(empregado, cardinalidade(1), particao(parcial)),
		    componente(dependente, cardinalidade(n), particao(total)) ).
relacionamento( dependentesDe,
		    componente(dependente, cardinalidade(n), particao(total)),
			componente(empregado, cardinalidade(1), particao(parcial)) ).


relacionamento( controla,
		    componente(departamento, cardinalidade(1), particao(parcial)),
		    componente(projeto, cardinalidade(n), particao(total)) ).
relacionamento( controla,
		    componente(projeto, cardinalidade(n), particao(total)),
			componente(departamento, cardinalidade(1), particao(parcial))).

relacionamento( trabalhaPara,
		    componente(departamento, cardinalidade(1), particao(total)),
       	    componente(empregado, cardinalidade(n), particao(total)) ).
relacionamento( trabalhaPara,
		    componente(empregado, cardinalidade(n), particao(total)),
			componente(departamento, cardinalidade(1), particao(total))).

relacionamento( gerencia,
		    componente(departamento, cardinalidade(1), particao(total)),
		    componente(empregado, cardinalidade(1), particao(parcial)) ).
relacionamento( gerencia,
		    componente(empregado, cardinalidade(1), particao(parcial)), 
			componente(departamento, cardinalidade(1), particao(total))).

relacionamento( trabalhaEm,
		    componente(empregado, cardinalidade(n), particao(total)),
		    componente(projeto, cardinalidade(n), particao(total)) ).

relacionamento( supervisao,
		    componente(empregado, cardinalidade(1), particao(parcial)),
		    componente(empregado,  cardinalidade(n) , particao(parcial)) ).
relacionamento( supervisao,
		    componente(empregado,  cardinalidade(n) , particao(parcial)),
			componente(empregado, cardinalidade(1), particao(parcial))).





/* ****************************** REGRAS PARA O ESQUEMA CONCEITUAL ************************ */

atributoDe(X, tipoChave, Y) :- chaveDe(X,Y).

entidade(X) :- eFraca(X); eForte(X).

chaveParcialDe(Y,X) :- eFraca(X), chaveDe(Y, X). %nao eh necessaria na tarefa de conversao

/* ****************************** REGRAS PARA O ESQUEMA RELACIONAL ************************ */

relaciona(A,B) :- relacionamento(_, componente(A, _, _), componente(B, _, _)).




/* ****************************** REGRAS PARA O MAPEAMENTO ENTRE OS ESQUEMAS ************************ */

relacao(X) :- entidade(X).

relacao(R) :- relacionamento(R, componente(_, A1, _) , componente(_, B1, _)) , 														(A1 == cardinalidade(n)), (B1 == cardinalidade(n)). 

relacao(Y) :- atributoDe(Y, tipoMultivalorado, X) , entidade(X). 


atributoRelDe(X, Z) :- entidade(Z), atributoDe(X,Y,Z), not(Y == tipoMultivalorado), not(Y == tipoCalculado).

atributoRelDe(AT, A) :- relacionamento(R, componente(A, A1, A2), componente(_, B1, _)) , 
							(A1 == cardinalidade(1)) , (B1 == cardinalidade(1)) , (A2 ==particao(total)) , atributoDe(AT, _, R).

atributoRelDe(AT, B) :- relacionamento(R, componente(_, A1, A2), componente(B, B1, _)) , 
							(A1 == cardinalidade(1)) , (B1 == cardinalidade(n)) , (A2 ==particao(total)) , atributoDe(AT, _, R).

atributoRelDe(AT,R) :- relacionamento(R, componente(_, cardinalidade(n), _) , componente(_, cardinalidade(n),_)) , atributoDe(AT, _, R).

atributoRelDe(renomeacao(Y),Y) :- atributoDe(Y, tipoMultivalorado, X) , entidade(X). 

chavePrimariaDe(Y,X) :- chaveDe(Y,X), eForte(X).

chaveEstrangeiraDe(C,A) :- relaciona(A,B) , chaveDe(C,B) , eForte(B) , eFraca(A).

chaveEstrangeiraDe(C,A) :- relacionamento(_, componente(A, A1, A2) , componente(B, B1, _)) , 												(A1 == cardinalidade(1)), (B1 == cardinalidade(1)), chaveDe(C,B) , (A2 == particao(total) ).

chaveEstrangeiraDe(C,B) :- relacionamento(_, componente(A, A1, _) , componente(B, B1, _)) , 												(A1 == cardinalidade(1)), (B1 == cardinalidade(n)), chaveDe(C,A).

chaveEstrangeiraDe(C1,R) :- relacionamento(R, componente(A, cardinalidade(n), _) , componente(_, cardinalidade(n), 									_)) , chaveDe(C1, A).

chaveEstrangeiraDe(C2,R) :- relacionamento(R, componente(_, cardinalidade(n), _) , componente(B, cardinalidade(n), 									_)) , chaveDe(C2, B).

chaveEstrangeiraDe(Z, Y) :- chaveDe(Z, X), atributoDe(Y, tipoMultivalorado, X), entidade(X).

referencia(componenteRel(C,A),componenteRel(C,B)) :- relaciona(A,B), chaveDe(C,B), eForte(B), eFraca(A).

referencia(componenteRel(C,A),componenteRel(C,B)) :- relacionamento(_, componente(A, A1, A2) , componente(B, B1, _)) , 						(A1 == cardinalidade(1)), (B1 == cardinalidade(1)), chaveDe(C,B) , (A2 == particao(total) ).

referencia(componenteRel(C,B),componenteRel(C,A)) :- relacionamento(_, componente(A, A1, _) , componente(B, B1, _)) , 												(A1 == cardinalidade(1)), (B1 == cardinalidade(n)), chaveDe(C,A).

referencia(componenteRel(C1,R),componenteRel(C1,A)) :- relacionamento(R, componente(A, cardinalidade(n), _) , 								componente(_, cardinalidade(n), _)) , chaveDe(C1, A).

referencia(componenteRel(C2,R),componenteRel(C2,B)) :- relacionamento(R, componente(_, cardinalidade(n), _) , 								componente(B, cardinalidade(n), _)) , chaveDe(C2, B).

referencia(componenteRel(Z, Y), componenteRel(Z, X)) :- chaveDe(Z, X), atributoDe(Y, tipoMultivalorado, X), entidade(X).

chaveCompostaDe(X,Y) :- chaveDe(X,Y) , eFraca(Y).

chaveCompostaDe(X,Y) :- eFraca(Y), chaveEstrangeiraDe(X,Y).

chaveCompostaDe(C1,R) :- relacionamento(R, componente(A, cardinalidade(n), _) , componente(_, cardinalidade(n), 									_)) , chaveDe(C1, A).

chaveCompostaDe(C2,R) :- relacionamento(R, componente(_, cardinalidade(n), _) , componente(B, cardinalidade(n), 									_)) , chaveDe(C2, B).

chaveCompostaDe(Z, Y) :- chaveDe(Z, X), atributoDe(Y, tipoMultivalorado, X), entidade(X).

chaveCompostaDe(renomeacao(Y), Y) :- atributoDe(Y, tipoMultivalorado, X), entidade(X).





















