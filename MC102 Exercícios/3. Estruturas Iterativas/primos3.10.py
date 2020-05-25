""" No exemplo dos números primos visto em aula, não precisamos testar todos os números entre 2 e (n-1) para verificar se dividem ou não n. Basta testarmos até n/2. Por quê? Qual o maior divisor possível de ? Na verdade basta testarmos os números 2 até sqrt(n). Por quê? """

""" Suponha que d/n e d>sqrt(n) --> n/d=K --> K<sqrt(n) e K é inteiro

1  2 ... K ... l sqrt(n) (l+1)... d ... (n-1) n 

Só é necessário testar de 1 até srqt(n) """

n = int(input('Insira um número: ')

for i in range 

