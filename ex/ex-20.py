pesoD = 0
menor = 0
for i in range(0,5):
    peso = float(input('informe seu peso '))
    if peso > pesoD:
        pesoD = peso 
    else:
        menor = peso
print(pesoD)