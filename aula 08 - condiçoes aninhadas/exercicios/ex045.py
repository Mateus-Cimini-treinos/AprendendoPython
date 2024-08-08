# faça um algoritimo que e um jogo de jokenpo
import random

player = int(input('escolha uma opçao \n [ 1 ] Pedra \n [ 2 ] Papel \n [ 3 ] Tesoura\n   '))
pc = random.randint(1,3)

if player == pc :
    print('empatou')
elif player == 1 and pc == 3 :
    print('Voce jogou PEDRA e o computador jogou TESOURA! VOCE GANHOU')
elif player == 2 and pc == 1 :
    print('Voce jogou PAPEL e o computador jogou PEDRA! VOCE GANHOU')
elif player == 3 and pc == 2 :
    print('Voce jogou TESOURA e o computador jogou PAPEL! VOCE GANHOU')
elif pc == 1 and player == 3 :
    print('Voce jogou TESOURA e o computador jogou PEDRA! VOCE PERDEU')
elif pc == 2 and player == 1 :
    print('Voce jogou PEDRA e o computador jogou PAPEL! VOCE PERDEU')
elif pc == 3 and player == 2 :
    print('Voce jogou PAPEL e o computador jogou TESOURA! VOCE PERDEU')
else:
    print('voce digitou a opçao errada')