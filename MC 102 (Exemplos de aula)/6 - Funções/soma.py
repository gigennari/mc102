#constante do nosso programa 
INCREMENTO = 3      #escopo global/convenção: escrever em letra maiúscula

def somar(x):       #usamos verbos para o nome de funções
    x = x + INCREMENTO
    return x        #devolve valor para a função main

def main():
    x = int(input("Digite um número: "))
    soma1 = somar(x)
    INCREMENTO = 4      #como não está no escopo global, a função somar ainda vai usar incremento=3
    soma2 = somar(x)   
    x = somar(x)
    y = somar (x)       #o x aqui já foi alterado pela função somar
    print(soma1)        
    print(soma2)      
    print(y)    

main()