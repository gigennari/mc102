def funcao(arg1, arg2):
    print(f'o primeiro argumento é {arg1}')
    print(f'o primeiro argumento é {arg2}')
    

def main():
    lista = ['josé', 'ana']
    funcao(*lista)


main() 