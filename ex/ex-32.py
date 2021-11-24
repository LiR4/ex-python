listaCPF = []
multi = 0
for i in range(11):
    listaCPF.append(input('informe seu CPF (Só números) '))

for n in range(10, 2):
    for c in listaCPF:
        d1 = c * n 

        if c.isdigit():
            multi = multi +d1

print(multi)