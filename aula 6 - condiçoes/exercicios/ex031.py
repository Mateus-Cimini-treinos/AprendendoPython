#crie um algoritimo que recebe a distancia da viagem e devolve o valor da passagem caso a distancia for menor a 200km R$ 0.50 por km se for maior que 200 R$ 0.45 por km

distance = int(input('Qual a distancia da viagem? '))

if distance <= 200 :
    print('Valor do km é 50 centavos')
    price = distance * 0.5
    print ('O preço da pasagem é R${:.0f}'.format(price))
else :
    print('valor do km e 45 centavos')
    price = distance * 0.45
    print('O preço da passagem e de R$ {:.0f}'.format(price))