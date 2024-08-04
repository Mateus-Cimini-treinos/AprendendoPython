# Aula de modulos/bibliotecas em Python

#importando a biblioteca math que e uma biblioteca focada funçoes matematicas
import math

number = float(input('Digite um numero '))

#criando um variavel que recebe a raiz quadrada da variavel number
root = math.sqrt(number)
print('A raiz quadrada de {} e: {:.2f}'.format(number, root))

#criando um variavel que recebe o valor da variavel number arrendodada para cima
roundUp = math.ceil(number)
print('O numero: {}, arrendodado para cima fica {:.2f}'.format(number,roundUp))

#criando um variavel que recebe o valor da variavel number arrendodada para baixo 
roundDown = math.floor(number)
print('O numero: {}, arrendodado para baixo fica {:.2f}'.format(number, roundDown))

#criando um variavel que recebe o valor da variavel number de forma truncada sem casas decimais 
trunc = math.trunc(number)
print('O numero: {} de forma truncada sem as casas decimais fica: {}'.format(number, trunc))

#criando um variavel que recebe o valor de number e devolve o fatorial 
factorial = math.factorial(int(number))
print('O fatorial de: {} e: {:.2f}'.format(number, factorial))  

#criando um variavel que recebe o valor de number e devolve a potencia 
power = math.pow(number, 2)
print('A potencia de {} e: {:.2f}'.format(number, power))

print('--' * 50)
'''---------------------------------------------------------------------------------------------------------------------'''
#importando a biblioteca random que e uma biblioteca focada em gerar numeros aleatorios
import random

# variavel rand vai receber um numero aleatorio entre 1 e 10
rand = random.randint(1, 10)
print(rand)

print('--' * 50)
'''---------------------------------------------------------------------------------------------------------------------'''

#importando a biblioteca emoji que e uma biblioteca focada em gerar emojis
import emoji
#fazendo um print com o emoji de joia
print(emoji.emojize('Olha o joinha :thumbs_up:'))


print('--' * 50)
'''---------------------------------------------------------------------------------------------------------------------'''