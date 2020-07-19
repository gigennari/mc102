"""
Maior divisor comum 
"""

def mdc(num1, num2):
    """ Devolve o maior divisor comum entre dois numeros"""
    if num1 == num2:
        return num1
    elif num1 > num2:
        return mdc(num1 - num2, num2)
    else:
        return mdc(num2-num1, num1)


def main():
    num1 = int(input())
    num2 = int(input())

    print(f"O mdc de {num1} e {num2} é {mdc(num1, num2)}")


main()