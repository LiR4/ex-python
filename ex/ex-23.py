from random import randint

soma = 0

for i in range(0,11):
    ran = randint(1,10)
    print(ran)
    soma = soma + ran
print(soma)