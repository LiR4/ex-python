X = 0
while X != 1:
    altura = float(input('qual sua altura '))
    sexo = str(input('informe seu sexo, (F) feminino e (M) masculino '))
    if sexo == 'F':
        peso = (62.1 * altura) - 58
        print ('seu peso ideal é {}' .format(peso))
    elif sexo == 'M':
        peso = (72.7 * altura) - 58
        print ('seu peso ideal é {}' .format(peso))

    X = int(input('deseja continuar ? se sim digite (1) e se não digite um numero diferente de (1)'))