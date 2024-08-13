#faça um programa que recebe a largura e a altura de um terreno e retorna sua area

def area(l,a):
    tot = l * a
    print(f'Um terreno com {l} metros de largura e {a} metros de altura tem a area de {tot} metros quadrados')


def titulo(msg):
    print('-=-' *20)
    print(msg)
    print('-=-'*20)


titulo('     Tamanho Àrea')
area(l=float(input('Qual a largura do terreno? ')), a=float(input('Qual a altua do terreno? ')))


titulo()
area()
