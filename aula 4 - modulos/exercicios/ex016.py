# crie um programa que recebe um numero com casas decimais e retorna ele inteiro

import math

num = float(input('Digite um numero '))

roundDown = math.floor(num)

print('O inteiro do numero {} é: {} !'.format(num, roundDown))