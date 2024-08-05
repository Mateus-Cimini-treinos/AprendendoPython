#faça um codigo que recebe o tamanho dos catetos do triangulo e retorna o tamanho da hipotenusa

import math

cathetusA = float(input('Comprimento do cateto oposto? '))
cathetusB = float(input('Comprimento do cateto adjacente? '))

hypotenuse = math.hypot(cathetusA, cathetusB)

print('O comprimeto da hipotenusa é: {:.2f}'.format(hypotenuse))