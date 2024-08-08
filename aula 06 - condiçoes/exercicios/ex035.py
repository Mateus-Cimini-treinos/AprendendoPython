#crie um programa que recebe o comprimento de 3 linhas e diz se e possivel forma um triangulo com essas linhas 

line1 = float(input('Qual o comprimento da primeira linha? '))
line2 = float(input('Qual o comprimento da segunda linha? '))
line3 = float(input('Qual o comprimento da terceira linha? '))

if line1 + line2 > line3 and line2 + line3 > line1 and line1 + line3 > line2 :
    print('Da para fazeer um triangulo')
else :
    print('Nao da')