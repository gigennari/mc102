"""
Escreva um programa que lê um número n,
e então imprime o menor número primo que é maior ou igual n,
e imprime o maior primo que é menor ou igual a n. 1

"""
import math 

def eh_primo(n):
    divisores =[]
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            divisores.append(d)
        else:
            pass 
    if len(divisores) == 0:
        return True
    else:
        pass 


def main():
    n = int(input("Insira um número "))      #ler numero     
    x = n-int(math.sqrt(n))
    y = n+int(math.sqrt(n))
    if eh_primo(n):                         #se n for primo, devolver ele
        print(f"{n} é primo")
    else:
        for i in range(x, n):   #chechar qual é p primeiro numero entre n-raiz de n e n que é primo
            if eh_primo(i):                    #quando achar, print, continue
                print(f"O maior primo menor que {n} é {i}")
                continue
        for i in range(n, y):      #checar qual é o primeiro numero entre n e n+raiz de n
            if eh_primo(i): 
                print(f"O menor primo maior que {n} é {i}")
                break

main() 

 
    
    
        