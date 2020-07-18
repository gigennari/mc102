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
    parser.add_argument("--evento", help="identificador do evento.", default= None, type=int)
    parser.add_argument("acao", help="ação sobre a agenda.", type=string)
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
    with open(nome_arquivo) as arquivo:
        arquivo.write(str(agenda))
    

def encontrar_evento(evento):
    pass 

def criar_evento(agenda):
    pass 

def alterar_evento(agenda, evento):
    """Procura evento, altera dict dentro do dict"""
    pass

def remover_evento(agenda, evento):
    pass

def listar_eventos(agenda, data):
    pass


def main():
    agenda = ler_agenda(args.a)
    if args.acao == "inicializar":
        inicializar_agenda(agenda)
    elif args.acao == "criar":
        criar_evento(agenda):
    elif args.acao == "alterar":
        alterar_evento(agenda, args.evento):
    elif args.acao = "remover":
        remover_evento(agenda, args.evento)
    elif args.acao == "listar":
        listar_eventos(agenda, args.data)
    
main()
