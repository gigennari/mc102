""" o input lê uma string, ou seja, 
lê uma linha na codificação utf-8 
(cada letra equivale a um byte)

Na leitura de um arquivo, 
quando a string termina no \n,
aparece um erro EOFError
End of file error

"""

linha1 = input()       
print(f"A primeira linha é {linha1}")

linha2 = input()
print(f"A segunda linha é {linha2}")