#faça um algoritimo que gera um numero secreto e o usuario da um chute e o algoritimo gera uma mensagem dizendo que ele acertou ou erro

import random

num = random.randint(1, 5)

kick = int(input('Chute um numero  '))

if kick == num :
    print('Voce acertou!! Voce tem muita sorte')
else :
    print('Voce errou!!')