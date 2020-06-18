"""

Entrada: nota em cada uma das tarefas e a presença do estudante
em cada uma das aulas

tarefa0 A tarefa1 C tarefa2 B
faltou
presente
presente
faltou

Saída: "Aprovadx", se cumpriu todos os critéios 
        "Reprovadx", caso caontrário 

Critérios de aprovação:
1)ter 75% de frequencia
2)obter pelo menos conceito C em todas as tarefas
(ou seja, se aparecer pelo menos um D, já está reprovado)

"""

def receber_dados():
    lista_de_lista_dados = []
    while True:
        try:
            dado = input().split()
            lista_de_lista_dados.append(dado)
        except EOFError: 
            break 
    return lista_de_lista_dados  #obtemos uma lista do tipo [['tarefa0', 'A', 'tarefa1', 'B'], ['faltou'], ['presente']]

def obter_lista_notas(lista_de_lista):
    """ Percorre a primeira lista da lista de entrada, como no enunciado. Toda 'tarefa'assume índice par e nota, ímpar. 
    Logo, adicionamos à lista de notas, apenas os indices ímpares. """
    lista_notas = []
    lista_tarefas_notas = lista_de_lista[0]
    for i, dado in enumerate(lista_tarefas_notas):
            if i % 2 == 1:
                lista_notas.append(dado)
    return lista_notas

def obter_lista_presenca(lista_de_lista):
    """obter uma lista contendo apenas 'presente' ou 'faltou'; ela se inicia 
    na posição 1 da lista de lista até o final""" 
    lista_presenca = lista_de_lista[1 : len(lista_de_lista)]
    return lista_presenca

def nenhum_D(lista):
    """Percorre a lista de notas para verificar se não há notas D, um criério de reprovação.
    Caso haja, retorna False"""
    nenhum_D = True 
    for i, nota in enumerate(lista):
        if nota == 'D':
            nenhum_D = False
    return nenhum_D 

def presenca_maior_75(lista):
    """Percorre a lista de presença. Conta faltas em uma variável. 
    Se numero de faltas > 0,25 * total de aulas (tamanho lista), retorna False"""
    quantidade_faltas = 0
    for i, dado in enumerate(lista):
        if dado == ['faltou']:
            quantidade_faltas += 1
    if quantidade_faltas > (0.25 * len(lista)):
        return False 
    else:
        return True 


def main():
    dados_aluno = receber_dados()
    lista_notas = obter_lista_notas(dados_aluno) 
    lista_presenca = obter_lista_presenca(dados_aluno)
    nota_OK = nenhum_D(lista_notas)
    presenca_OK = presenca_maior_75(lista_presenca)
    if nota_OK and presenca_OK:  #se os dois critérios de aprovação forem cumpridos
        print('Aprovadx')   
    else:
        print('Reprovadx')


main()