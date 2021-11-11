import math 

X = 0

while X != 'N':
    med = float(input('Informe o tamanho da parede em metros quadrados '))
   
    litros = med / 3

    lata18 = litros / 18
    lata36 = litros / 3.6

    preco1 = lata18 * 450
    preco2 = lata36 * 190

    print('o valor com ', lata18 , 'latas com 18 litros, no preço de ', preco1  )
    print('o valor com ', lata36 , 'latas com 3.6 litros, no preço de ', preco2 )

    X = str(input('se deseja sair digite (S) e se não (N)'))

