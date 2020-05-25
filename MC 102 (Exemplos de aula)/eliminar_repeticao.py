def eliminar_repeticao(lista1, lista2):
    lista_sem_rep = []
    freq_sem_rep = []
    for i in range(len(lista1)):
        if lista1[i] not in lista_sem_rep:
            lista_sem_rep.append(lista1[i])
            freq_sem_rep.append(lista2[i])
    return lista_sem_rep, freq_sem_rep

def main():
    lista1 = [3, 3, 6, 5, 8, 8, 10]
    lista2 = [2, 2, 1, 1, 2, 2, 1]
    lista3, lista4 = eliminar_repeticao(lista1, lista2)
    print(lista3)

main()