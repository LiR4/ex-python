import PySimpleGUI as sg

def janela_inicial():
    sg.theme("Reddit")
    layout = [
        [sg.Text('insira a placa na caixa a baixo ')],
        [sg.Input(key="placa")],
        [sg.Button('Ok')]
    ]
    return sg.Window("Verificar", layout=layout, finalize=True)

def janela_MA():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Placa valida')],
        [sg.Text('Placa modelo antigo')],
        [sg.Button('Recomeçar'), sg.Button('Sair')] 
    ]
    return sg.Window("Resultado", layout=layout, finalize=True)

def janela_MS():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Placa valida')],
        [sg.Text('Placa modelo do mercosul')],
        [sg.Button('Recomeçar'), sg.Button('Sair')] 
    ]
    return sg.Window("Resultado", layout=layout, finalize=True)

janela1 = janela_inicial()
janela2 = None
cont = int
contA = int
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if  event == 'Ok':
        cont = None
        contA = None
        for car in values["placa"]:
            if car.isdigit():
                cont +=1
            elif car.isalpha():
                contA += 1
        if contA == 3 and cont == 4:
            janela2 = janela_MA()
        elif contA == 4 and cont == 3:
            janeala2 = janela_MS()

    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Recomeçar':
        janela1 = janela_inicial()
    if window == janela2 and event == 'Sair':
        break
