''' crie um algoritimo que recebe o ano de nacimento de um homem e retorna
se ele ainda nao tem idade para se alistar ou
tem idade para se alistar ou
ja passou da idade para se alistar


e o algoritimo tmb deve dizer quanto tempo falta ou quanto tempo ja passou
a idade aceitavel para se alistar nesse codigo foi usado entre 18 a 45 anos de idade
'''
#importando biblioteca
from datetime import date

#definiundo data de hj
today = date.today()
currentYear = today.year


#input do ano de nacimento
yearBirth = int(input('Em que ano voce naceu? '))

#definindo sua idade
age = currentYear - yearBirth
print('Voce tem {} anos'.format(age))

if age < 18 :
    print('voce ainda e muito novo para servir')
    difference = age - 18
    difference = abs(difference)
    print('ainda falta {} anos'.format(difference))
elif age > 45 :
    print('voce ja passou da idade de servir')
    difference = 45 - age
    difference = abs(difference)
    print('vc esta {} anos atrasado'.format(difference))
else:
    print('voce esta na idade de servir')