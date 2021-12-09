from random import randint

cont = 0

Dn = {
    1234:['lira',10.0],
    123:['marcos',8.0],
    420:['rodrigo',6.0]
}

def notas():
    cod = randint(0,5000)
    nome = str(input('informe o nome do aluno '))
    nota = float(input('informe a nota do aluno'))
    Dn.update({cod:[nome,nota]})

    notaA = sorted(Dn.items())
    
    for i in notaA:
        print(i[0], i[1])

def att():
        codT = int(input('informe o código do aluno a ser atualizado'))
        nomeA = str(input('informe o nome do aluno a ser atualizado '))
        NotaA = float(input('informe a nota atualizada'))
        
        for Name in Dn.keys():
            codi = int(Name)
            if codi == codT:
                Dn.update({codT:[nomeA, NotaA]})
                print(Dn)

def ver():
        codv = int(input('informe o código do aluno para mostrar a nota do aluno '))
        for code in Dn.keys():
            codi = int(code)
            if codi == codv:
                print(Dn[code])

def exe():
        codv = int(input('informe o código do aluno para deletar o aluno da lista '))
        for code in Dn.keys():
            codi = int(code)
            if codi == codv:
                del Dn[code]
                print('aluno deletado')
                
def med():
    notac = sorted(Dn.values())
    me = 0
    cont = 0
    for i in notac:
        no = i[1]
        me += 1
        cont = cont + no
    
    Media = cont / me
    print('A média da turma é ', Media)

def ex():
    while True:
        print('olá o que gostaria ??')
        print('1 = lista de notas / 2 = inserir nota do aluno / 3 = atualizar nota / 4 = consultar a nota do aluno / 5 = apagar aluno da lista / 6 = media da turma / para sair digite (S)')
        action = str(input())
        if action == '1':
            print(Dn)
        elif action == '2':
            notas()   
        elif action == '3':
            att()
        elif action == '4':
            ver()
        elif action == '5':
            exe()
        elif action == '6':
            med()
        elif action == 's' or action == 'S':
            break

print(ex())