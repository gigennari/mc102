
#para cada índice i de texto
    #para cada indice j de padrão
        #comparte texto[i+j] e padrao[j]

def verifica_padrao(texto, padrao):
    for i in range(len(texto)):
        encontrei_padrao = True 
        for j in range(len(padrao)):
            if texto[i+j] != padrao[j]:
                encontrei_padrao = False 
                break

        if encontrei_padrao:
            return True
        else:
            return False

def main():
    texto = input()
    padrao = input()
    padrao = verifica_padrao(texto, padrao)
    if padrao:
        print('Há padrão')
    else:
        print("Não há padrão")

main()

