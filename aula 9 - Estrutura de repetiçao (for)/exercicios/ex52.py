#crie um programa que recebe um numero e diz se ele e primo

num = int(input('\n\033[mDigite um numero '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else :
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2 :
    print('\n\033[mO numero {} foi divisivel {} vezez ele e primo'.format(num, tot))
else:
    print('\n\033[mO numero {} foi divisivel {} vezez ele nao e primo'.format(num, tot))