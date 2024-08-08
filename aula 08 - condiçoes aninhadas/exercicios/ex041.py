#crie um algoritimo que recebe a data de nacimento do nadador e diz se ele esta em qual categoria
'''
ate 9 anos = mirim
ate 14 anos = infatil
ate 19 anos = junior
ate 20 anos = senior
acima de 20 = master

'''

#importando biblioteca
from datetime import date

#definiundo data de hj
today = date.today()
currentYear = today.year


#input do ano de nacimento
yearBirth = int(input('Em que ano voce naceu? '))




age = currentYear - yearBirth

if age <= 9 :
    print('Sua categoria e Mirim pq vc tem {} anos'.format(age))
elif age > 9 and age <= 14  :
    print('Sua categoria e Infatil pq vc tem {} anos'.format(age))
elif age > 14 and age <= 19  :
    print('Sua categoria e Junior pq vc tem {} anos'.format(age))
elif age > 19 and age <= 20  :
    print('Sua categoria e Senior pq vc tem {} anos'.format(age))
else :
    print('Sua categoria e Master pq vc tem {} anos'.format(age))