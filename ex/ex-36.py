while True:
    horaI = int(input('informe a hora '))
    minI = int(input('informe os minuntos '))
    def hora():
       if horaI < 11 and minI <= 59:
           print(hora, ':', minI, 'AM')
       else:
            conta = horaI - 12
            print(conta, ':', minI, 'PM')
        
    print(hora())
    sair = int(input('deseja sair 1 para sair e 0 para continuar '))
    if sair == 1:
        break
    
