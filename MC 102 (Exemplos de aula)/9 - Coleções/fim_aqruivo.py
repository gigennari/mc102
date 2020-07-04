linha1 = input()
print(f'Li a linha 1: {linha1}')

linha2 = input()
print(f'Li a linha 2: {linha2}')

i = 1
while i < 10000000:
    if i % 1000000 == 0:
        print(i)
    i += 1



#   fechando o arquivo de entrada padrão (sinalizar fim do aqruivo)

#   1) no bash (*nix): ctrl + D 

#   2) no windows    : ctrl + Z, Enter