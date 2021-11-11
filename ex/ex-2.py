nota = 0

pessoas = float(input('Quantas pessoas vão viajar ? '))
diaP = (input('compraram a passagem 3 dias antes do embarque (S) para sim (N) ? '))
diaria = float(input('quantos dias irão ficar '))
at = float(input('Os dois tiveram a autorização para ferias (1) para sim (2) para não '))
filho = (input('Tem filhos (S) para sim (N) para não '))
if filho == 'S':
    nota = float(input('informe a nota do filho ')) 

salario = (input('O salario foi liberado antes do dia 12 de dezembro (S) para sim (N) para não '))

if diaP == 'S':
    total = 1100 * pessoas
    diar = 566.66 * diaria
    totalFull = total + diar 
else:
    total = 890 * pessoas
    diar = float(566.66 * diaria)
    totalFull = total + diar 
if at == 1:
    atv = 'A'
else:
    atv = 'B'


if nota >= 6:
    notaV = 'A'
else:
    notaV = 'B'

if salario == 'S':
    salarioV = 'A'
else:
    salario = 'B'  

if totalFull <= 10000:
    NaN = 'A'
else:
    NaN = 'B'

if atv == 'A' and notaV == 'A' and salarioV == 'A' and NaN == 'A':
    print('Pode viajar filho')
else:
    print('Num pode')

print('Valor total: %d'  %totalFull)