nomes = input('Insira os nomes: ').split()

iniciais=[]
for nome in nomes:
    inicial = nome[0]   #pega a primeira letra
    if inicial not in iniciais:   #evita iniciais repetidas
        iniciais.append(inicial)
print("  ".join(iniciais))
    