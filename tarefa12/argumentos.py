"""
Implementar um aplicativo de agenda em modo texto

Usuário pode:
inicializar agenda
criar evento
alterar informaçãoes do evento
remover evento
listar todos os eventos de um dia 

CSV --> valores separados por vírgulas 

sys.argv é uma lista de strings com os argumentos 
 
Para o usuário fazer uma operação sobre a agenda, ele passará
opção -a com o nome do arquivo CSV da agenda + argumento do programa
a ação correspondente (inicializar, criar, alterar, remover, listar)

Devolver uma mensagem, informando que a ação foi realizada
Para listar, saída compatível com os exemplos do teste

AGENDA = {1: {nome: "" , descricao: "", data: "", hora: ""}, 2: {}, 3:{}}

"""

import sys
import argparse 

#usar default None ou ""? 
parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--agenda", help="nome de sua agenda.", type=string)
    parser.add_argument("--evento", help="identificador do evento.", default= None, type=int)   #evento é inteiro, será a chave do dict agenda
    parser.add_argument("acao", help="ação sobre a agenda.", type=string)   #não tem --, é digitada diretamente no terminal 
    parser.add_argument("--nome", help="nome do evento.", default= None, type=string)
    parser.add_argument("--descricao", help="descrição do evento.", default= None, type=string)
    parser.add_argument("--data", help="data do evento xx/xx/xxxx.", default= None, type=string)
    parser.add_argument("--hora", help="hora do evento xx:xx.", default= None, type=string)

    args = parser.parse_args() 

def ler_agenda(nome_arquivo):
    """Lê arquivo agenda.csv e cria um dict de dicts agenda com eventos"""
    str_agenda = ""
    with open('nome_arquivo') as arquivo:
        str_agenda = arquivo.readline()
    agenda = eval(str_agenda)
    return agenda 

def inicializar_agenda(nome_arquivo):
    """Apenas cria arquivo agenda.csv"""
    with open('nome_arquivo', 'w') as arquivo:
    return 

def escrever_arquivo_agenda(nome_arquivo, agenda):
    with open('nome_arquivo', 'w') as arquivo:
        arquivo.write(str(agenda))
    
def encontrar_evento(agenda, identificador):
    """Recebe o número do evento e devolve o dict do evento"""
    for evento in agenda:
        if evento == identificador:     #se chave == numero do evento
            return agenda[evento]       #devolve o valor da chave do evento
    return None

def criar_evento(agenda, nome, descricao, data, hora):
    """ Cria um novo evento e adiciona ele na agenda"""
    #cria dict do evento
    evento = {
        "nome": nome, 
        "descricao": descricao, 
        "data": data, 
        "hora": hora
    }

    #como a chave dos eventos não muda quando deletamos um evento, queremos add o novo evento
    #no numero mais alto possível que ainda não existe no dict, para não apagar outro evento
    numero_existentes = agenda.keys()   
    numero_novo = max(numero_existentes) + 1
    
    agenda[numero_novo] = evento    #add dict do evento no dict de eventos
    return agenda

def alterar_evento(agenda, identificador):
    """Procura evento, altera dict dentro do dict"""

    pass

def remover_evento(agenda, identificador):
    """Remove um evento da agenda pelo numero dele; o numero dos demais 
    eventos permanece o mesmo"""
    agenda.pop(identificador)  #evento é o inteiro chave de agenda 
    return agenda 

def listar_eventos(agenda, data):
    """ Encontra e imprime na tela todos os eventos da agenda na data inserida pelo usuário """

    eventos = []
    numero_eventos = []
    identificadores = agenda.keys   #precisamos das chaves para acessar os eventos e para saber o numero deles na hora de imprimir

    for identificador in identificadores:
        if agenda[identificador]['data'] == data:
            eventos.append(dicio[identificador])    #lista recebe dicts dos eventos 
            numero_eventos.append(identificador)    #lista recebe numero do evento


    if len(eventos) == 0:   #se len é 0, não há eventos
        print(f"Não existem eventos para o dia {data}!")
    else:
        print(f"Eventos do dia {data}\n")
        print("-----------------------------------------------\n")
        for i in range(len(eventos):
            print(f"Evento {numero_eventos[i]} - {eventos[i]['nome']}")
            print(f"Descrição: {eventos[i]['descricao']}")
            print(f"Data: {eventos[i]['data']}")
            print(f"Hora: {eventos[i]['hora']}")
            print("-----------------------------------------------")


def main():
    agenda = ler_agenda(args.a)
    if args.acao == "inicializar":
        inicializar_agenda(args.a)
    elif args.acao == "criar":
        criar_evento(agenda, args.nome, args.descricao, args.data, args.hora):
        escrever_arquivo_agenda(agenda)    
    elif args.acao == "alterar":
        alterar_evento(agenda, args.evento)
        escrever_arquivo_agenda(agenda)
    elif args.acao = "remover":
        remover_evento(agenda, args.evento)
        escrever_arquivo_agenda(agenda)
    elif args.acao == "listar":
        listar_eventos(agenda, args.data)
    else:
        print(f"Operação {args.acao} é inválida")
    
main()
