vasco = []
vascop = []
cont = 0
d2 = 0   
for i in range(11): 
    vasco.append((input('informe o cpf ')))

vascop.append(vasco)
vasco.pop(10)
vasco.pop(9)

for c in vasco:
    cont = cont + 1
    C = int(c)
    d1 =  C * (11  - cont)
    d2 = d2 + d1

digi1 = (d2 * 10 ) % 11

vasco.append(digi1) 

cont = 0
d2 = 0
d1 = 0
C = 0

for c in vasco:
    cont = cont + 1
    C = int(c)
    d1 =  C * (12 - cont)
    d2 = d2 + d1

digi2 = (d2 * 10 ) % 11

vasco.append(digi2)

print(vasco)