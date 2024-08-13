#crie um programa que tem um input que so aceita valores int sem usar o int(input('...'))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!! Digite um numero valido.\033[m]')
        if ok:
            break
    return valor



n = leiaInt('Digite um numero ')
print(f'Voce acabou de digitar o numero {n} !')