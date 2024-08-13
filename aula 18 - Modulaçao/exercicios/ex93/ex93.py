#melhore o programa do ex 92 criando uma funçao moeda() melhorando a formataçao do texto

from modulo import moeda

preço = float(input('Qual o preço? R$'))
print(f'''
O valor do produto e: {moeda.moeda(preço)} 
O valor em dobro e: {moeda.moeda(moeda.dobro(preço))} 
A metade do valor e: {moeda.moeda(moeda.metade(preço))}
aumentando 10% temos: {moeda.moeda(moeda.aumentar(preço))}
diminuindo 13% temos: {moeda.moeda(moeda.diminuir(preço))}
''')