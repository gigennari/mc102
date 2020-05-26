""" 
Faça um programa que recebe uma sequência de números inteiros
positivos e retorna a soma dos quadrados dos numero primos dessa
sequência. 

Se a sequencia for vazia ou não tiver nenhum primo, a saída
deve ser 0. 

Entrada: 2 3 5 5 8

2, 3, 5, 5 são primos. Ao quadrado, 4, 9, 25, 25. Somados 63.

Saída: 63 



mapeia(lista, quadrado)
    valor_reduzido = reduz(lista, somar_elementos)

"""

def eh_primo(numero):
    encontrei_divisor = False
    for i in range(2, numero):
        if numero % i == 0:
            encontrei_divisor = True
            break

    if not encontrei_divisor and numero > 1: #para ser True, not e False --> se o número não tiver divisor sem ser ele mesmo ou 1
        numero_eh_primo = True               #numero é primo, retorna True 
    else:
        numero_eh_primo = False              #numero não é primo, retorna False
    return numero_eh_primo 

def filtrar(lista, funcao):
    lista_nova =[]
    for i, numero in enumerate(lista):
        if funcao(numero):              #se o elemento em questao não for primo
            lista_nova.append(numero)
    return lista_nova
    
def quadrado(numero):
    quadrado = numero ** 2
    return quadrado
    
def mapeia(lista, funcao):
    for i in range(len(lista)):
        lista[i] = funcao(lista[i]) 
    return lista 

def somar_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def reduz(lista, funcao):
    valor_reduzido = funcao(lista)
    return valor_reduzido
    
def main():
    lista = input().split() 
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    lista = filtrar(lista, eh_primo)
    lista = mapeia(lista, quadrado)
    valor = reduz(lista, somar_elementos)
    
    print(valor)


main()