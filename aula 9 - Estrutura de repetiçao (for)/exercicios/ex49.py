#crei um programa que refaça o exercicio 9 usando for


number = int(input('Digire um numero: '))
for c in range (0, 11):
    r = c * number
    print('{} X {} = {}'.format(number,c,r))
print('fim')


