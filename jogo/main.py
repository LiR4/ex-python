import PySimpleGUI as sg

def janela_inicial():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Qual é seu nome")],
        [sg.Input()],
        [sg.Button("Continuar")]
    ]
    return sg.Window("Inicio", layout=layout, finalize=True)
def janela_part0():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Olá, se prepare para aventura" )],
        [sg.Text("Você está em uma caverna e avista um dragão, mas ao lado dele a um pote de ouro ")],
        [sg.Text("O que você faz ?" )],
        [sg.Text('                               ')],
        [sg.Text("Esolha uma das opções ")],
        [sg.Text('                               ')],
        [sg.Text("Se aproximar.. "), sg.Button('A')],
        [sg.Text("Sair correndo.. "), sg.Button('B')]
    ]
    return sg.Window("entrando na aventura", layout=layout, finalize=True)
def janela_part1A():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Você se aproxima do dragão e ele continua a dormir, você vai em direção ao ouro ")],
        [sg.Text("                                                   ")],
        [sg.Text("O que você ira fazer ??")],
        [sg.Text("Pega o ouro e sai correndo..."), sg.Button('A')],
        [sg.Text("Você não pega o ouro e vai embora..."), sg.Button('B')],
    ]
    return sg.Window("parte 1", layout=layout, finalize=True)
def janela_part1B():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Você ganhou!!")],
        [sg.Text("             ")],
        [sg.Text("Você saiu vivo da caverna e viveu feliz com sua familia ")]
    ]
    return sg.Window("YOU WIN!!", layout=layout, finalize=True)

janela1, janela2 = janela_inicial(), None

while True:
    window,event,values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == "Continuar":
        janela2 = janela_part0()
        janela1.hide()
    
    if window == janela2 and event == 'A':
        janela3 = janela_part1A()
        janela2.hide()
    if window == janela2 and event == 'B':
        janela3 = janela_part1B()
        janela2.hide()