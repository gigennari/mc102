Instruções elementares permitidas:

1. criar e atualizar variáveis
2. armazenar listas
3. identificar se um número está contido em uma lista 
4. interpretar condições 
5. criar e aplicar funções 
6. somar 
7. dividir apenas números inteiros
8. identificar o resto de uma divisão
9. retornar valores 



Algoritmo:

definir lista meses31 (01, 03, 05, 07, 08, 10, 12)
definir lista meses30  (04, 06, 09, 11)
criar variáveis dia, mês, ano, diasdecorridos, x
 
definir x como 0
tomar nota de dia, mês, ano, diasdecorridos 

definir função SOMAR DIAS1:
se dia < x
	somar 1 a dia
modificar dia para 1
	se mês = 12
		modificar mês para 1
		somar 1 a ano
	somar 1 a mês

definir função SOMAR DIAS2:
se dia < x
	somar 1 a dia
modificar dia para 1
somar 1 a mês



repetir  diasdecorridos-1  vezes

	se mês estiver contido na lista meses31
		definir x como 31
		executar SOMAR DIAS1

	caso contrário
		se mês estiver contido na lista meses30
		    definir x como 30
		    executar SOMAR DIAS2

		caso contrário
			se resto (ano÷4)=0 e resto de (ano÷100) ≠ 0 OU  resto (ano÷400)=0
				definir x como 29
				executar SOMAR DIAS2

			caso contrário
			definir x como 28
			executar SOMAR DIAS2


retornar dia, mês e ano

