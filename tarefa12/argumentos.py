"""
Implementar um aplicativo de agenda em modo texto

Usuário pode:
criar evento
alterar informaçãoes do evento
remover evento
listar todos os eventos de um dia 

Evento = identificador, nome, descrição, data, hora

CSV --> valores separados por vírgulas 


sys.argv é uma lista de strings com os argumentos 

Argumento 0: argumentos.py
Argumento 1: argumento
Argumento 2: outro
Argumento 3: argumento com espaços
Argumento 4: -o

Para o usuário fazer uma operação sobre a agenda, ele passará
opção -a com o nome do arquivo CSV da agenda + argumento do programa
a ação correspondente (inicializar, criar, alterar, remover, listar)

Devolver uma mensagem, informando que a ação foi realizada
Para listar, saída compatível com os exemplos do teste

"""

import sys
import argparse 

#usar default None ou ""? 
parser = argparse.ArgumentParser()
    parser.add_argument("programa", help="Programa para executar.", type=string)
    parser.add_argument("-a", "--agenda", help="nome de sua agenda.", type=string)
    parser.add_argument("--evento", "--identificador", help="identificador do evento.", type=int)
    parser.add_argument("ação", help="ação sobre a agenda.", type=string)
    parser.add_argument("--nome", "--nome", help="nome do evento.", type=string)
    parser.add_argument("--descricao", "--descricao", help="descrição do evento.", type=string)
    parser.add_argument("--data", "--data", help="data do evento xx/xx/xxxx.", type=string)
    parser.add_argument("--hora", "--hora", help="hora do evento xx:xx.", type=string)

    args = parser.parse_args()

    resultado = math.log(args.numero, args.base)

def ler_entrada():
    entrada = input()
    for i, argumento in enumerate(sys.argv):
        print(f"Argumento {i}: {argumento}")    #armazenar em uma Classe?


def ler_agenda(a):
    """Lê arquivo agenda.csv e cria um conjunto agenda com eventos"""
    pass 

def inicializar_agenda():
    pass 

def criar_evento(agenda, evento):
    pass 

def alterar_evento():
    pass

def remover_evento(agenda, evento):
    pass

def listar_eventos(agenda, data):
    pass


def main():
    entrada = ler_entrada()
    

main()
