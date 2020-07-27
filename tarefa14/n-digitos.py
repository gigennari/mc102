"""
Dado um valor n e uma soma s, o programa encontra todas as combinações de 
n dígitos (0-9) cuja soma dos dígitos é s. 

Imprime em ordem crescente. 

Ideia:
Supondo que tenhamos n=3 e s=3

Caso básico = se s=0, não tem solução 

1) PRIMEIRO DÍGITO: de 1 a 9 
soma = 3
loop usando 1
1 --> soma -= 1

2) SEGUNDO ao Nesimo DÍGITO: de 0 a 9 --> RECURSIVO 

soma = 2
0 --> soma = 2, continuar 

soma=2
vai fazer com 0, não vai chegar na soma 3
vai fazer com 1, soma ainda vai ser 1
vai fazer com 2, soma == 0
devolve o 102
"""



def combinacoes(n_digitos, soma):
    lista = []
    if n_digitos == 2:
        for i in range(0,10):
            k = soma - i
            if k in range(0, 10):
                numero = str(i) + str(k)
                lista.append(numero)
    else:
        for i in range(0, 10):
            if soma - i >= 0:
                for possibilidade in combinacoes(n_digitos - 1, soma - i):
                    numero = str(i) + str(possibilidade)
                    lista.append(numero)
    return lista

def imprimir(lista_combinacoes, n_digitos):
    lista_sem_zeros = []
    for combinacao in lista_combinacoes:
        valor = int(combinacao)
        string = str(valor)
        if len(string) < n_digitos:
            pass
        else:
            print(combinacao)

            


def main():
    entrada = input().split()
    n_digitos = int(entrada[0])
    soma = int(entrada[1])

    lista_combinacoes = combinacoes(n_digitos, soma)
    imprimir(lista_combinacoes, n_digitos)

main()