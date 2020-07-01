def obter_lista_presenca(lista, indice):
    """obter uma lista contendo apenas 'presente' ou 'faltou'; ela se inicia 
    na posição do último coneceito encotrado + 1""" 
    indice_incio = indice + 1
    lista_presenca = lista[indice + 1 : len(lista)]
    return lista_presenca


def main():
    lista = ['tarefa0', 'A', 'tarefa1', 'C', 'tarefa2', 'C', 'faltou', 'presente', 'faltou', 'faltou', 'presente']
    indice = 5
    lista_presenca = obter_lista_presenca(lista, indice)
    print(lista_presenca)

main()