""" No exemplo dos números primos visto em aula, não precisamos testar todos os números entre 2 e (n-1) para verificar se dividem ou não n. 
Basta testarmos até n/2. Por quê? Qual o maior divisor possível de ? 
Na verdade basta testarmos os números 2 até sqrt(n). Por quê? """

""" Suponha que d/n e d>sqrt(n) --> n/d=K --> K<sqrt(n) e K é inteiro

1  2 ... K ... l sqrt(n) (l+1)... d ... (n-1) n 

Só é necessário testar de 1 até srqt(n)

 """
import math

n = int(input('Insira um número: '))
divisores =[]

for d in range(2, int(math.sqrt(n))+1):
    if n % d == 0:
        divisores.append(d)
    else:
        pass 

if len(divisores) == 0:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} NÃO é primo")

