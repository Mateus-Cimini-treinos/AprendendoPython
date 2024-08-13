#melhore o programa do ex92 e ex93 fazendo que as funçoes receba um parametro se elas vao ser ou nao usadas 

from modulo import moeda

preço = float(input('Qual o preço? R$'))
print(f'''
O valor do produto e: {moeda.moeda(preço)} 
O valor em dobro e: {moeda.dobro(preço, True)} 
A metade do valor e: {moeda.metade(preço, True)}
Aumentando 10% temos: {moeda.aumentar(preço, True)}
Diminuindo 13% temos: {moeda.diminuir(preço, True)}
''')