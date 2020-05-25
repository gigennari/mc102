""" n <-- leia um número do teclado
divisores <-- crie uma lista vazia
para d de 2 até n - 1:
    se d divide n:
        adicione d aos divisores
devolva divisores"""

n = int(input('Isira um numero: '))


for d in range (2, n):
    if n % d == 0:              
        divisor_encontrado = True
        break                         #se não fizer break o programa continua avaliando os proximos números

    else:
        divisor_encontrado = False

if n == 1 or divisor_encontrado:
    print('O número é 1 ou tem divisores não triviais')
else:
    print('O número é primo')