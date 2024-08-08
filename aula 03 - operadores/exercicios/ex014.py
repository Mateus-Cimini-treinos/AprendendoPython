'''crie um algoritimo que converte Celsius para Fahrenheit'''

temp = float(input("Temperatura em celsius: "))


f = temp * 1.8 + 32

print('A temperatura em celsius era de: {:.2f}\n em fahrenheit fica {:.2f}\n'.format(temp, f))