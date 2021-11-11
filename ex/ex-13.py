X = 0

while X != 'N':
    horas = int(input('digite quantas horas trabalhadas '))
    Ph = float(input('digite o valor por hora '))
    dia = horas * Ph
    sal = dia * 22
    
    salL = sal / 1.24 

    salI = sal / 1.11
    salim = sal - salI

    sals = sal / 1.08
    salsin = sal - sals

    salsii = sal / 1.05
    salsi = sal - salsii

    print('total ', sal)
    print('pago a imposto de renda %.2f' % salim)
    print('pago a o inss %.2f' % salsin)
    print('pago a o sindicato %.2f' % salsi)
    print('O salario liquido foi de %.2f' % salL)

    X = str(input('deseja continuar ? se sim digite (S) e se não (N) '))
