#crie um programa queelabora um preço total do produto levando em conta o preço e o metodo de pagamento
'''
1 avista no dinheiro/cheque = 10% de desconto
2 avista no cartao = 5 %de desconto
3 em ate 2 vezez no cartao = preço normal
4 dividir em mais de 3X no cartao = 20% de juro

'''

price = float(input('Qual o valor do produto? '))
payment = int(input('Qual o metodo de pagamento?\n [ 1 ] A vista noo dinheiro ou pix\n [ 2 ] A vista no cartao\n [ 3 ] No cartao em 2X\n [ 4 ] No cartao em mais de 3X  '))

if payment == 1 :
    payment1 = price - (price * 10 / 100)
    print('O valor do produto é {} com o desconto de 10% foi para {}'.format(price,payment1))
elif payment == 2 :
    payment2 = price - (price * 5 / 100)
    print('O valor do produto é {}com o desconto de 5% foi para {}'.format(price,payment2))
elif payment == 4 :
    num = int(input('Voce vai pagar em quantas parcelas?'))
    payment4 = price + (price * 20 / 100)
    paymentNum = payment4 / num
    print('O preço do produto e de {} com os juros de 20% o preço ficou {} e o valor da parcela vai ser de {}'.format(price,payment4,paymentNum))
elif payment == 3 :
    payment3 = price / 2
    print('O preço do produto e de {} e o valor da parcela e de {}'.format(price, payment3))
else:
    print('Opçao errada')
    