#melhore o programa criando uma funçao no modulo dado chamada leiadinheiro() que seja capaz de funcionar como a funçao input()  mas que aceite dados em formataçao monetaria
from utilidades.moeda import moeda
from utilidades.dados import dado

preço = dado.leiadinheiro('Qual o preço? R$')
moeda.resumo(preço)