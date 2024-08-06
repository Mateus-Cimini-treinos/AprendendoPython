''' crie um programa para calcular bo imc

< 18.5 : abaixo do peso
>= 18.5 e < 25 : peso ideal
>= 25 < 30 : sobrepeso
>= 30 <= 40 : obsidade
> 40 ? obsidade mórbida

'''

#inputs
weight = float(input('Seu peso em kg: '))
height = input('Sua altura em centímetros: ')

#formatando a altuta para esta na formataçao de exemplo (1.70)
if '.' not in height:
    height = height[:-2] + '.' + height[-2:]

#tranformando altura em float e calculando o imc
height = float(height)
imc = weight / (height * height)


if imc < 18.5 : 
    print('Seu imc e {}! E esta abaixo do peso'.format(imc))
elif imc > 18.5 and imc < 25 : 
    print('Seu imc e {}! E esta com peso normal'.format(imc))
elif imc >= 25  and imc < 30 : 
    print('Seu imc e {}! E esta com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40 : 
    print('Seu imc e {}! E esta com obesidade'.format(imc))
else :
    print('Seu imc e {}! E esta com obesidade móbida'.format(imc))