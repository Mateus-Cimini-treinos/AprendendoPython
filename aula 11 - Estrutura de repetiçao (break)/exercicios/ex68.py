#crie um programa que jogue par ou impar com vc se vc ganhar vc joga dnv ate perder, e ele fala quantas vezes vc ganhou

import random

cont = 0
while True:
    computador = random.randint(0,1)
    cont += 1
    jogador = int(input('Qual seu número? '))
    resultado = computador + jogador

    imparOuPar = str(input('Você quer par ou ímpar? [P/I] ')).upper()

    if resultado % 2 == 0:
        par = True
        impar = False
    else:
        par = False
        impar = True

    if imparOuPar == 'P':
        if par:
            print('Jogador venceu')
            perdeu = False
        else:
            print('Jogador perdeu')
            perdeu = True

    elif imparOuPar == 'I':
        if impar:
            print('Jogador venceu')
            perdeu = False
        else:
            print('Jogador perdeu')
            perdeu = True

    if perdeu:
        cont -= 1
        break

print(f'Acabou voce perdeu!! vc ganhou {cont} vezes')
