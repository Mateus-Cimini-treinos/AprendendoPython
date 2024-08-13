# melhore o programa criando um pacote chamado utilidades que tenha 2 modulos internos chamados moeda e dado
# transfira todas as funçoes dos ex anteriores para o modulo moeda e mantenha fucionando  

from utilidades.moeda import moeda

preço = float(input('Qual o preço? R$'))
moeda.resumo(preço)