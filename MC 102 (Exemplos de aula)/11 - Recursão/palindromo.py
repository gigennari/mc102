"""
Palavras que de trás pra frente são iguais a palavra 

radar
arara
reviver
ame o poema
a sacada da casa

Casos básicos:
primeira letra diferente da última -- > False
uma letra ou 0 letras(serve para avaliar palavras de tamanho par) --> True
Caso geral: 
checar dos dois extremos
"""

def eh_palindromo(p):
    if len(p) <= 1:
        return True 
    elif p[0] != p[-1]:
        return False
    else:
        return eh_palindromo(p[1:-1])


def main():
    palavra = str(input('digite uma palavra: ')).replace(" ", "")

    resultado = eh_palindromo(palavra)

    if resultado == True:
        print(f"{palavra} é um palindromo")
    else:
        print(f"{palavra} não é um palindromo")

main()