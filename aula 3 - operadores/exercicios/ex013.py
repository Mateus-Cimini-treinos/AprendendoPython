''' crie um algoritimo que recebe um valor e devolve com 15% de aumento'''

wage = float(input('Qual o seu salario? R$ '))

rise = wage + 15 / 100 * wage
print('O seu salario e de R$ {} e depois do aumento de 15% vai ficar R${}'.format(wage,rise))