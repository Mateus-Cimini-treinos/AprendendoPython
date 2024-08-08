#crie um programa que recebe um numero no input 1 e outro no input 2 e diz qual input recebeu o maior

num1 = float(input('Digite o valor da Opçao 1 >> '))
num2 = float(input('Digite o valor da Opçao 2 >> '))

if num1 == num2 :
    print('Ambos tem o mesmo valor')
elif num1 > num2 :
    print('A Opçao 1 e maior que a opçao 2')
else:
    print('A opçao 2 e maior que a opçao 1')