def fatorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

digit = int(input('numero para mostra o fatorial '))

print(fatorial(digit))