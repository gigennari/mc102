"""
Esse programa calcula a quantidade de número primos até um número n

Para n muito grande, o programa demora MUITO tempo para executar

real - tempo total gasto, incluindo tempo que eu gastei para ler a 
mensagem na tela, digitar o numero n e dar enter
user - tempo, de fato, gasto para resolver o problema 
sys - tempo que o sistema operacional utiliza para responder a chamada 
do programa 

n=100       user    0m0,025s
n=10000     user    0m2,713s
n= 100000   user    4m37,849s   #muuuuuito tempo
"""

def eh_primo(p):
    if p == 0 or p == 1:
        return False

    tem_divisor = False
    for divisor in range(2, p):
        if p % divisor == 0:
            tem_divisor = True

    if tem_divisor:
        return False
    else:
        return True

def contar_primos(n):
    m = 0
    for p in range(n):
        if eh_primo(p):
            m+=1

    return m 

def main():
    n = int(input('Digite o número n: '))
    m = contar_primos(n)
    print(f'Há {m} primos de 0 ate {n-1}')

main()