#faça um algoritimo que recebe um angulo qualquer e retorne o valor do seno cosseno e tangente
import math

angle = float(input('Quantos graus tem o angulo? '))


radianAngle = math.radians(angle)

sine = math.sin(radianAngle)
cosine = math.cos(radianAngle)
tangent = math.tan(radianAngle)

print('O angulo que vc informou era de {} graus!\nO angulo radiante tem {:.2f} graus!\nO comprimento do seno é: {:.2f} !\nO comprimento do cosseno é: {:.2f} !\nO comprimento da tangente é: {:.2f} !'.format(angle, radianAngle, sine, cosine, tangent))