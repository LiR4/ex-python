X = 0
while X != 1:
    kilo = float(input('Informe a quantidade de kilos de peixe '))
    
    if kilo > 50:
        kilom = kilo - 50.00
        multa = 40.00 * kilom
        print('vai pagar ', multa, 'de multa ')
    else:
        print ('não há multa a pagar ')

    X = int(input('digite (1) para sair se não digite outro numero '))