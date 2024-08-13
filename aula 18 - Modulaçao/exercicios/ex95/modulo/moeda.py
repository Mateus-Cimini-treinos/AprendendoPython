def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else moeda(res)

def diminuir(preço = 0, formato = False):
    preçoComDesconto = preço - (13 / 100) * preço
    return preçoComDesconto if formato is False else moeda(preçoComDesconto)

def aumentar(preço = 0, formato = False):
    preçoComJuros = preço + (10 / 100) * preço
    return preçoComJuros if formato is False else moeda(preçoComJuros)

def moeda(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0) :
    print('-' *30)
    print('Resumo do Valor'.center(30))
    print('-' *30)
    print(f'''
O valor do produto e: \t{moeda(preço)} 
O valor em dobro e: \t{dobro(preço, True)} 
A metade do valor e: \t{metade(preço, True)}
Aumentando 10% temos: \t{aumentar(preço, True)}
Diminuindo 13% temos: \t{diminuir(preço, True)}
''')
    print('-' *30)