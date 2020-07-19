"""
Suponha que queremos cortar um pedaço de papel retangular, 
digamos, para fazer um cartão ou um bilhete. É bem provável que 
não exista folha disponível na papelaria com exatamente esse 
tamanho. Então precisamos descobrir qual o menor formato de 
papel em que cabe nosso retângulo.

A0 --> 2 A1 --> 4 A2 --> 8 A3 --> 16 A4

A1 --> 1/2 A0

A0 --> 841mm largura X 1189mm altura
A1 --> 594             841
A2 --> 420             594
A3 --> 297             420
A4 --> 210             297
A5 --> 148             210

Suponha que recemos uma A0 e queremos descobrir qual o menor subtipo
da A0 que cabe um retangulo de largura w e altura h.

Suponha h >= w

Entrada: h, w, tipo da folha, larg da folha, altura da folha 

Saída: numero do papel

Casos:

1) se for maior que A0 --> None 
2) caso básico --> w > w_folha ou h > h_folha (se não couber em uma dimensão, não adianta, por isso, OU)
3) caso geral --> w <= w_folha ou h <= h_folha
se for menor, corta o papel no meio e verifica se ainda cabe 
se couber, corte de novo; caso contrario é aquele papel 

O qur fazemos:
1) criamos uma folha menor de 
altura =  w_folha
largura = h_folha // 2
tipo_menor = tipo + 1
2) resolvemos recursivamente
    se n cabe na menor, devolve
    se cabe, 


""" 

LARGURA_A0 = 841
ALTURA_A0 = 1189

def menor_subtipo(w_folha, h_folha, tipo, w, h):
    """ Devolve o menor subtipo da folha em que cabe o retângulo """

    if w > w_folha or h > h_folha:
        return None 
    else:
        #cria instância menor 
        h_menor = w_folha
        w_menor = h_folha // 2
        tipo_menor = tipo + 1

        #se não cabe na folha menor
        if w > w_menor or h > h_menor:
            return tipo_menor 
        else:
            return menor_subtipo(w_menor, h_menor, tipo_menor, w, h)



def main():
    larg_retangulo = int(input('digite a largura do retângulo: '))
    alt_retangulo = int(input('digite a altura do retângulo: '))

    tipo = menor_subtipo(LARGURA_A0, ALTURA_A0, 0, larg_retangulo, alt_retangulo)

    print(f"Utilize um papel A{tipo}")

main()