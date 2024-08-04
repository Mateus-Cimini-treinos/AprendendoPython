''' faça um programa que recebe um numero e devolve o antecessor e sucessor'''

number = int(input('Digite um numero: '))

before = number - 1

after = number + 1

print('O numero que vc digitou é: {} \nSeu antecessor é: {} \nSeu sucessor é: {}'.format(number, before, after))