import os
cancel = 0
while cancel == 0:
    cont = 0
    contA = 0

    placa = str(input('digite a sua placa '))

    for car in placa:
        if car.isdigit():
            cont = cont + 1
        elif car.isalpha():
            contA = contA + 1

    if contA == 3 and cont == 4:
        print('placa aceita ')
        print('placa modelo antigo ')
    elif contA == 4 and cont == 3:
        print('placa aceita ')
        print('placa modelo do mercosul')
    else:
        print('placa invalida')
    
    cancel = str(input('Se for continuar pressione ENTER se não (1)'))
    
    os.system('cls') or None
          