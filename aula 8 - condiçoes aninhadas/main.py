# Aula sobre condiçoes aninhadas if,elif e else


car = str(input('Qual modelo do seu carro? '))



if car == 'Golf':
    print('Nossa, vc tem um carro maneiro')
elif car == 'Celta' or car == 'Gol' or car == 'Uno':
    print('Seu carro e muito popular no Brasil')
elif car in 'Palio Ciena Tipo ':
    print('Seu carro e da fiat')
else: 
    print('Nao conheço seu carro')
    

print('Voce tem um {}!'.format(car))

