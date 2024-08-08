#melhore o codigo do ex 28, agora o jogador vai jogar ate acertar e quando terminar vai aparecer a mensagem dizendo que acertou e quantas tentativas vc teve

import random

num = random.randint(1, 10)
cont = 0
kick = 11
while kick != num :
    kick = int(input('Chute um numero  '))
    cont += 1
    if num > kick :
        print('Voce chutou baixo')
    elif kick > num :
        print('Voce chutou alto')
if kick == num :
    print('Voce acertou!! Voce tem muita sorte\n O numero era {} e vc chutou {} ate acertar'.format(num, cont))

    

