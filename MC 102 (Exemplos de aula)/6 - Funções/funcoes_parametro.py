PI = 3.1415

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def aplicar_bonus_generico(notas_provas, bonus, funcao_operacao):
    n = len(notas_provas)
    for i in range(n):
        notas_provas[i] = funcao_operacao(notas_provas[i], bonus)
    return notas_provas


def main():
    notas_provas = [8.5, 7.3, 4.0, 8.4]
    bonus_aditivo = 0.5
    bonus_multiplicativo = 1.1
    bonus_divisao = 3.0
    aplicar_bonus_generico(notas_provas, bonus_aditivo, soma)
    aplicar_bonus_generico(notas_provas, bonus_multiplicativo, multiplicacao)
    aplicar_bonus_generico(notas_provas, bonus_divisao, divisao)
    print(notas_provas)

main()