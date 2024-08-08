#crie um algoritimo que recebe o valor do salario do fucionario e se o mo salario for menor que 1250 recebe um aumento de 15% e se for maior que 1250 recebe um aumento de 10%

wage = float(input('Qual o salario do Fucionario? R$'))

increase1 = 10
increase2 = 15

if wage > 1250 :
    increase = wage * (1 + increase1 / 100)
    print('O salario era de {} mais os 10%\n foi para {:.2f}'.format(wage, increase))

else :
    increase = wage * (1 + increase2 / 100)
    print('O salario era de {} mais os 15%\n foi para {:.2f}'.format(wage, increase))
             