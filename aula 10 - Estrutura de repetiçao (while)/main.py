# Aula de loop mais especificamente (while)
# Para você testar o código remova os '''''' que estão entre o código que quer testar

# Loop simples de 0 a 10 com 'for'
'''for c in range(0, 11):
    print(c)
print('FIm')
'''

# Loop simples de 0 a 10 com 'while'
c = 0
'''while c < 11 :
    print(c)
    c += 1  # Incrementa o valor de c em 1 a cada iteração
print('Fim')
'''

# Loop que continua pedindo um valor até o usuário digitar 0
'''
n = 1
while n != 0 :
    n = int(input('Digite um valor:'))  # Pede ao usuário para digitar um valor
print('Fim')
'''

# Loop que continua pedindo um valor enquanto o usuário digitar 's'
'''
n = 's'
while n == 's' :
    int(input('Digite um valor:'))  # Pede ao usuário para digitar um valor
    n = str(input('Quer continuar? [N/S] ')).lower()  # Pergunta se o usuário quer continuar
print('Fim')
'''

# Loop que conta quantos números pares e ímpares foram digitados até o usuário digitar 0
'''
n = 1
par = 0
impar = 0
while n != 0 :
    n = int(input('Digite um valor:'))  # Pede ao usuário para digitar um valor
    if n != 0 :
        if n % 2 == 0 :  # Verifica se o número é par
            par += 1  # Incrementa a contagem de pares
        else:
            impar += 1  # Incrementa a contagem de ímpares
print('pares {} impares {}'.format(par, impar))  # Exibe a contagem de pares e ímpares
print('Fim')
'''
bre