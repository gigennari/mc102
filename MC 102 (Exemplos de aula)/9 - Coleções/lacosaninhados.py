
def funcao():

    def subfuncao():

        while True:
            for i in range(10):
                print(f'Estamos na iteração {i} do for')
                if i == 7:
                    return
    subfuncao()
    print('Depois da chamada da subfunção')        

funcao()
