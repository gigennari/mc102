n = int(input('Digite quantos amigos você tem:  '))
amigos = []
i = 0 

while i < n:
    nome = input(f'Digite o nome do amigo número {i+1}: ')
    amigos.append(nome)
    i += 1

j = int(input('Digite um número: '))
print (f'Seu amigo número {i-1} chama-se {amigos[j-1]}')
