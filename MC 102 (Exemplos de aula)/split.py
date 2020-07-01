
def main():

    variavel = input('Insira operacao: ')

    partes = []
    pos_ultimo_espaco = -1
    i = 0
    n = len(variavel)
    while i < n:
        if variavel[i] == ' ':
            parte = variavel[pos_ultimo_espaco+1 : i]
            pos_ultimo_espaco = i
            partes.append(parte)
        i += 1
            
    parte = variavel[pos_ultimo_espaco+1 : n]
    partes.append(parte)

    print(partes[1])

main() 