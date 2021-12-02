linha = str(input('digite uma palavra com no minimo 4 letras no maximo 10 '))

def vali():
    if len(linha) >= 4 and len(linha) <= 10:
        return True
    else:
        return False

print(vali())