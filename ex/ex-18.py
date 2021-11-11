from time import sleep

n = 0

for i in range(1,500, 2):
    if i % 3 == 0:
        n+= i

print("os numeros impares multiplos de 3 são ", n)      