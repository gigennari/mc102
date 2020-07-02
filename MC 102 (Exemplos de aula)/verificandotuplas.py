for i in range(len(tuplas)-1): 
        bits_iguais = bool(tuplas[i][0] == tuplas[i+1][0] and tuplas[i][1] == tuplas[i+1][1])
        if i <= len(tuplas) - 2:  
            if bits_iguais: 
                contador += 1
                proximo_igual = True
            else:
                lista_frequencia.append(contador)
                contador = 1
                lista_pares_finais.append(tuplas[i-1])
                proximo_igual = False 
        elif i == len(tuplas) - 1:
            if proximo_igual:
                if tuplas[-2] == tuplas[-1]:
                    lista_frequencia.append(contador+1)
                    lista_pares_finais.append(tuplas[-2])
                else:
                    lista_frequencia.append(contador)
                    lista_pares_finais.append(tuplas[-2])
                    lista_frequencia.append(1)
                    lista_pares_finais.append(tuplas[-1])
            else:
                if tuplas[-2] == tuplas[-1]:
                    lista_frequencia.append(2)
                    lista_pares_finais.append(tuplas[-2])
                else:
                    lista_frequencia.append(1)
                    lista_pares_finais.append(tuplas[-2])
                    lista_frequencia.append(1)
                    lista_pares_finais.append(tuplas[-1])
        else:
            break               