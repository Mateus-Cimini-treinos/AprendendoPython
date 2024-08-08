# faça um programa que refaça o ex51 usando o while

primeiro = int(input('primeiro termo: '))
razao = int(input(' razao da PA'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('fim')