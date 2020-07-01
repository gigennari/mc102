"""if i % 2 == 1:
            lista_conceitos.append(dado)
print(lista_conceitos)

"""

lista = ['tarefa0', 'A', 'tarefa1', 'C', 'tarefa2', 'C', 'faltou']

lista_conceitos = []

for i, dado in enumerate(lista):
    while dado != 'presente':
        print('não é presente')
        