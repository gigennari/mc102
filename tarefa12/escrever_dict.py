
def escrever_arquivo_agenda(nome_arquivo, agenda):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(agenda))

def main():
    dicio = {1:{"nome": "giovanna", "idade": 19}, 2:{"nome": "zé", "idade":20}}
    escrever_arquivo_agenda("meudicio.csv", dicio)

main()
