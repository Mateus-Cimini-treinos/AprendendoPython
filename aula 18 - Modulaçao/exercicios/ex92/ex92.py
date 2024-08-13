#crie um programa com um modulo chamado moeda.py que tem as funçoes#
#aumentar(), diminuir(), dobro() e metade()
#e o seu programa retorna esses valores

from modulo import moeda

n = float(input('Qual o preço? '))
print(f'''
O valor do produto e: R${n} 
O valor em dobro e: R${moeda.dobro(n)} 
A metade do valor e: R${moeda.metade(n)}
aumentando 10% temos: R${moeda.aumentar(n)}
diminuindo 13% temos: R${moeda.diminuir(n)}
''')