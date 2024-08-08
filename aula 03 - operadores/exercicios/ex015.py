'''crie um algoritimo que recebe a quantidade de dias que um carro foi alugado e a quantidade de quilometros rodados e devolve o valor a pagar lembrando que  a diaria e de 60 reais e o valor por km e de 0.15 reais'''

days = int(input('Quantos dias o carro foi alugado?'))

kms = float(input('Quantos km vc rodou? '))

priceDays = days * 60

priceKms = kms * 0.15

price = priceDays + priceKms

print('Lembrando que o valor da diaria e 60R$ e o valor do km rodado e de 0.15R$, voce usou o carro por {} diasE rodou {}Kms \nO valor da diaria foi de: {}R$ \nE o valor dos kms rodados e de: {}R$\nE o total a pagar e de {}R$'.format(days, kms, priceDays, priceKms, price))