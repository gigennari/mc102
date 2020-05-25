""" Escreva um programa que leia um número real x,
tire sua raiz e 
imprima o terceiro digito antes e após a virgula""" 


x = int(input('Insira um número: '))

import math
x = math.sqrt(x)    #tirando raiz de x

y = str(x)          #transformando x em str para analisar a posição do ponto do float


pos_vir = y.index('.')
def ter_dig_antes: 
ter_dig_antes = y[pos_vir - 3]
def ter_dig_depois: 
ter_dig_depois = y[pos_vir + 3] 

if x<100: 
    if len(x[:pos_vir])>=3:
        print(f'O terceiro digito após a vírgula é {ter_dig_depois}')
    else:
        print('O terceiro dígito após a vírgula é zero')
    print('O terceiro digito antes da vírgula é zero') 

else:
    print('no')

    
    
    
   

   
 
   