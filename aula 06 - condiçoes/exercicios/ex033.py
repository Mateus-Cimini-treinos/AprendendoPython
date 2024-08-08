#crie um algoritimo que receba 3 numeros e fala qual e maior ou qual e menor

num1 = int(input('Digite um numero '))
num2 = int(input('Digite um numero '))
num3 = int(input('Digite um numero '))


if num1 >= num2 and num1 >= num3 :
    print(' O maior numero é {}'.format(num1))
elif num2 >= num1 and num2 >= num3 :
    print('O maior numero é: {}'.format(num2))
else :
    print('O numero maior é {}'.format(num3))

if num1 <= num2 and num1 <= num3 :
    print('O menor numero é {}'.format(num1))
elif num2 <= num1 and num2 <= num3 :
    print('O menor numero é {}'.format(num2))
else :
    print('O menor numero é {}'.format(num3))