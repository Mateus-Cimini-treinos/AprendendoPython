# crie um programa que calcula o fatorial de um numero
# exemplo 5  = 5*4*3*2*1 = 120


num1 = 1 
num = int(input('Digite um numero para ser fatorizado '))
cont = num
while cont > 0 :
    num1 *= cont
    cont -= 1
    
print('A resposta e {}'.format(num1))
print('acabou')