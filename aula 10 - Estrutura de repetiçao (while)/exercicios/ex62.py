#crie um programa que melhore o exercicio anterior que mostrava 10 termos, a melhoria consiste em quando  mostar o termo a pessoa pode escolher mostarr mais termos

primeiro = int(input('primeiro termo: '))
razao = int(input(' razao da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('mais quantos termos? '))