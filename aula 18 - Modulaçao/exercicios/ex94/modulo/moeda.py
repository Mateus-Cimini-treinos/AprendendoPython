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