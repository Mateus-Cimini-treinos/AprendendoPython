#aula de funçoes em python



'''

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)



titulo('    Sou foda  ')
titulo('    Melhor botlaner')
titulo('    EZ')

'''

'''
def soma(a,b):
    c = a + b
    print(f'{a} + {b} = {c}')


soma(10, 20)

'''
'''
def soma(a,b):
    c = a + b
    print(f' {a} + {b} = {c}')


soma(30,5)
soma(2,5)
'''
'''
def mostra(*num):
    tam = len(num)
    print(f'recebi os numeros {num} e sao {tam} numeros')
    

mostra(2,5,8)
mostra(39,4)
mostra(2,56,7,89,12)
'''

'''
def dobra(list):
    pos = 0
    while pos <len(list):
        list[pos] *=2
        pos += 1

valores = [10,20,40,58,67]
dobra(valores)
print(valores)
'''


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(4,9)
soma(32,32)
soma(12,343,54)
soma(23,4,6,8)