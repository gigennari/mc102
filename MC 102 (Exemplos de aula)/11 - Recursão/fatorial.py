"""
Russian nested dolls 

FATORIAL DE n 

n! =
1           se n = 1
n*(n-1)     se n > 1  

"""


def fatorial(n):
    if n == 0:
        return 1
    else:
        return fatorial(n-1) * n


def main():
    for i in range(1, 11):
        print(f"{i}! = {fatorial(i)}")

main ()