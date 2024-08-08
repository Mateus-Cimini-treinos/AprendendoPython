''' crie um programa que recebe um numero e devolve o dobro,triplo e raiz quadrada'''


number = int(input('Digite um numero:'))

double = number * 2

triple = number * 3

squareRoot = number**(1/2)

print('O numero que você digitou: {} \nDobro: {} \nTriplo: {}\nRaiz quadrada: {:.2f}'.format(number, double, triple, squareRoot))

