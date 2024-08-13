def dobro(preço = 0):
    return preço * 2

def metade(preço = 0):
    return preço / 2

def diminuir(preço = 0):
    preçoComDesconto = preço - (13 / 100) * preço
    return preçoComDesconto

def aumentar(preço = 0):
    preçoComJuros = preço + (10 / 100) * preço
    return preçoComJuros

def moeda(preço = 0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')