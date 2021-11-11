nome = input('digite seu nome ')
while (len(nome) <= 3):
    nome = input('digite novamente nome menor que 3 caracteres ')

idade = int(input('digite sua idade '))
while idade <= 0 or idade > 150:
    idade = int(input('Digite novamente idade menor 0 ou maior que 150'))

sal = float(input('informe seu salario '))
while sal <= 0:
    sal =  float(input('digite novamente salario menor que 0 '))
    
sexo = str(input('digite seu sexo: (f) feminino (m) masculino '))
while sexo != 'F' and sexo != 'M':
    sexo = str(input('digite novamente indefinido '))

estado = str(input('informe o estado civil: (S) solteiro (C) casado (V) viuvo (D) divorciado (J) junto '))
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd' and estado != 'j':
    estado = str(input('digite novamente letra errada'))

print(nome)
print(idade)
print(sal)
print(sexo)
print(estado)