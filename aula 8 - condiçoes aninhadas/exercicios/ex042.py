#crie um algoritimo que refaça o exercicio 35 mas acresente a fucuinalidade de dizer se o triangulo se enquadra em qual das classificaçoes
'''
Equilátero: todos os lados são iguais
Isóceles: dois lados sao iguais
Escaleno: todos os lados diferentes
'''


line1 = float(input('Qual o comprimento da primeira linha? '))
line2 = float(input('Qual o comprimento da segunda linha? '))
line3 = float(input('Qual o comprimento da terceira linha? '))


if line1 + line2 > line3 and line2 + line3 > line1 and line1 + line3 > line2 :
    print('Da para fazeer um triangulo')
    if line1 == line2 and line1 == line3 :
        print('E um triangulo Equilatero!!')
    elif line1 == line2 and line1 != line3 and line2 != line3 :
        print('E um triangulo isóceles')
    elif line2 == line3 and line3 != line1 and line1 != line2 :
        print('E um triangulo isóceles')
    elif line1 == line3 and line1 != line2 and line2 != line3 :
        print('E um triangulo isóceles')
    else:
        print('E um triangulo Escaleno')
else :
    print('Nao da')