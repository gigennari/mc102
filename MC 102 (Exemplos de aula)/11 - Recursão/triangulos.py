"""
Quantos triângulos há em um castelo de carta de n andares?

"""
def triangulos(n):
    if n == 1:
        return 1
    elif n == 2:
        return 4
    else:
        return n + (2 * triangulos(n - 1)) - triangulos(n - 2)  #recursão -->  chamamos a função dentro da função 

def main():
    for i in range(1, 11):
        print(f"t({i}) = {triangulos(i)}")

main() 