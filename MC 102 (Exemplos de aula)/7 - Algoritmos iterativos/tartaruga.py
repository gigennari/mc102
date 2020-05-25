"""Uma tartaruga está a 40m de sua casa. 
No primeiro minuto, ela anda 1m, no segundo
1/2, no terceio 1/3m e assim por diante.
Em quanto tempo ela chegará até sua casa?"""


def tempo_gasto_tartaruga(distanciatotal):
    numero_passos = 0
    distancia = 0
    proxima_distancia = 1

    while distancia < distanciatotal:
        numero_passos += 1
        distancia += proxima_distancia
        proxima_distancia = 1.0 / (numero_passos + 1)       #serie divergente muito lenta 
        if numero_passos % 10000 == 0:
            print(distancia)
    return numero_passos


def main():
    tempo = tempo_gasto_tartaruga(30)
    print(f"O tempo gasto pela tartaruga foi {tempo} minutos")

main()