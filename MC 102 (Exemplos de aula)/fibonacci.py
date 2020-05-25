#Sequência de Fibonacci
#a some de dois elementos define o próximo


def fib(n):                    #cria uma função para calcular a sequência de fibonacci até n  
	a, b = 0, 1            #atribuição múltipla
	while a < n:           #laço de repetição 
		print(a, end=' ')
		a, b = b, a+b  #redefinindo a e b, ou seja, A vira o último B e B vira a soma dos últimos a e b
	print()

	
