# faça um algoritimo que recebe a velocidade de um carro e se ele estiver acima de 80km/h recebe uma multa que e de 7R$ por km acima de 80
print('┅' * 30)

speed = int(input('Qual a velocidade do carro? '))

if speed <= 80 :
    print('Voce esta na velocidade aceitavel')
else :
    print('Voce ultrapassou a velocidade maxima permitida na via')
    moreSpeed = (speed - 80)
    punishment = (moreSpeed * 7)
    print('E recebeu uma multa de {}R$'.format(punishment))
    

print('┅' * 30)
