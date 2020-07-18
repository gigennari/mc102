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

def ler_agenda(nome_arquivo):
    """Lê arquivo agenda.csv e cria um dict de dicts agenda com eventos"""
    str_agenda = ""
    with open(nome_arquivo, 'r') as arquivo:
        str_agenda = arquivo.read().strip()
       
    agenda = eval(str_agenda)
    return agenda 

def inicializar_agenda(nome_arquivo):
    """Apenas cria arquivo agenda.csv"""
    arquivo = open(nome_arquivo, 'w')    #ao abrir o arquivo, se ele não existe, é criado
    arquivo.write('{}')
    arquivo.close()

def escrever_arquivo_agenda(nome_arquivo, agenda):
    with open(nome_arquivo, 'w') as arquivo:
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
    
    if len(numero_existentes) == 0:
        numero_novo = 1
    else:
        numero_novo = max(numero_existentes) + 1
    
    agenda[numero_novo] = evento    #add dict do evento no dict de eventos
    return agenda

def alterar_evento(agenda, identificador, nome, descricao, data, hora):
    """Procura evento, altera dict dentro do dict"""
    evento = encontrar_evento(agenda, identificador) 
    
    #por default os parâmetros são None. Isso significa que eles não devem ser alterados, por isso o pass.
    if nome == None:
        pass
    else:
        evento['nome'] = nome
    if descricao == None:
        pass
    else:
        evento['descricao'] = descricao
    if data == None:
        pass
    else:
        evento['data'] = data
    if hora == None:
        pass
    else:
        evento['hora'] = hora

    agenda[identificador] = evento

    return agenda

def remover_evento(agenda, identificador):
    """Remove um evento da agenda pelo numero dele; o numero dos demais 
    eventos permanece o mesmo"""
    agenda.pop(identificador)  #evento é o inteiro chave de agenda 
    return agenda 

def listar_eventos(agenda, data):
    """ Encontra e imprime na tela todos os eventos da agenda na data inserida pelo usuário """

    eventos = []
    numero_eventos = []
    identificadores = agenda.keys()   #precisamos das chaves para acessar os eventos e para saber o numero deles na hora de imprimir

    for identificador in identificadores:
        if agenda[identificador]['data'] == data:
            eventos.append(agenda[identificador])    #lista recebe dicts dos eventos 
            numero_eventos.append(identificador)    #lista recebe numero do evento


    if len(eventos) == 0:   #se len é 0, não há eventos
        print(f"Não existem eventos para o dia {data}!")
    else:
        print(f"Eventos do dia {data}")
        print("-----------------------------------------------")
        for i in range(len(eventos)):
            print(f"Evento {numero_eventos[i]} - {eventos[i]['nome']}")
            print(f"Descrição: {eventos[i]['descricao']}")
            print(f"Data: {eventos[i]['data']}")
            print(f"Hora: {eventos[i]['hora']}")
            print("-----------------------------------------------")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--agenda", help="nome de sua agenda.",required=True, type=str)
    parser.add_argument("acao", help="ação sobre a agenda.", type=str)   #não tem --, é digitada diretamente no terminal 
   
    parser.add_argument("--evento", help="identificador do evento.", type=int)   #evento é inteiro, será a chave do dict agenda
    
    parser.add_argument("--nome", help="nome do evento.", default= None, type=str)
    parser.add_argument("--descricao", help="descrição do evento.", default= None, type=str)
    parser.add_argument("--data", help="data do evento xx/xx/xxxx.", default= None, type=str)
    parser.add_argument("--hora", help="hora do evento xx:xx.", default= None, type=str)

    args = parser.parse_args() 

    if args.acao == "inicializar":
        inicializar_agenda(args.agenda)
    else:
        agenda = ler_agenda(args.agenda)
        if args.acao == "criar":
            agenda = criar_evento(agenda, args.nome, args.descricao, args.data, args.hora)  #devolve agenda com novo evento
            escrever_arquivo_agenda(args.agenda, agenda) #escreve agenda no arquivo csv
        elif args.acao == "alterar":
            agenda = alterar_evento(agenda, args.evento, args.nome, args.descricao, args.data, args.hora)    #devolve a agenda com evento alterado
            escrever_arquivo_agenda(args.agenda,agenda) #escreve agenda no arquivo csv
        elif args.acao == "remover":
            agenda = remover_evento(agenda, args.evento) #devolve agenda sem o evento
            escrever_arquivo_agenda(args.agenda, agenda) #escreve agenda no arquivo csv
        elif args.acao == "listar":
            listar_eventos(agenda, args.data)   #apenas lista eventos da data, não altera a agenda
        
main()
