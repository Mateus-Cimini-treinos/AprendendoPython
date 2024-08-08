'''crie um algoritimo que recebe um valor e devolve ele com 5% a menos como se fosse um desconto'''

price = float(input('Qual o preço R$'))

sale = price - (5 / 100) * price

print('O valor que digitou e: {:.2f}\n com 5% desconto fica R${:.2f}'.format(price, sale))

