# aula 2 de funçoes de python



# nesse cofigo eu fiz uma calculadora de fatorial que nao precisa ser mudada para fazer diferente teste oque muda e o input e exit que para testar e so retirar os '''''' em volta do bloco
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


'''
n = int(input('Digite um numero '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')
'''


'''
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados sao {f1}, {f2} e {f3}')
'''

#
def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else :
        return False

num = int(input('DIgite um numero '))
if parOuImpar(num) == True :
    print(f'O numero {num} e par')
if parOuImpar(num) == False :
    print(f'O numero {num} e impar')
