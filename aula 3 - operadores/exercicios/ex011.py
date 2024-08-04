'''crie um algoritimo que recebe a altura e largura de uma parede em metros e calcula quantos litros de tintas vao ser necessario para pintar sabendo que cada litro de tinta pinta 2m quadrados'''

width = float(input('Qual a largura da parede?'))
heigth = float(input('Qual a altura da parede?'))

metroQuadrado = width * heigth

tinta = metroQuadrado / 2

print(' a altura e; {}\n a largura e: {}\n a area da parede e {:.2f} metros quadrados \n e vai gastar {:.2f} litros de tinta'.format(heigth, width, metroQuadrado, tinta))