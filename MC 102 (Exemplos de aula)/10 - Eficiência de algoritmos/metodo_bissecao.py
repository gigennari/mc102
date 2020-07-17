"""
Objetivo: encontrar um aporximação da raíz de uma função contínua f(x)
TEOREMA DO VALOR INTERMEDIÁRIO (TVI)
Suponha que f(a)<0 e f(b)>0, se f(x) é contínua, 
haverá um f(c)=0 tal que a<c<b.


"""

ERR0 = 0.00000001

def f(x):
    return x**2 - 2

def metodo_bissecao(a, b, funcao):
    while b - a > ERR0:
        m = (a + b) / 2
        if funcao(m) < 0:
            a = m
        else:
            b = m
    return m


def main():
    a = 0.0
    b = 4.0
    y = metodo_bissecao(a, b, f)
    print(f"f({y}) = {f(y)}")

main () 
