#crie um programa que recebe um numero e pergunta para o usuario para qual base de convversao ele quer? binario,octal ou hexadecimal

num = int(input('Digite um numero para ser convertido  '))

metodo = int(input('Qual metodo vc quer?\nDigite 1 para binario\nDigite 2 para octal\nDigite 3 para hexadecimal\nOpiçao:  '))


if metodo == 1 :
    binario = bin(num)
    print('seu numero em binario fica assim {}'.format(binario[2:]))
elif metodo == 2 :
    octal = oct(num)
    print('seu numero em octal fica assim {}'.format(octal[2:]))
elif metodo == 3 :
    hexadecimal= hex(num)
    print('seu numero em hexadecimal fica assim {}'.format(hexadecimal[2:]))
else: 
    print('Opçao invalida')



