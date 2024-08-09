# crie um programa que recebe 4 valores e guarda em uma tupla e depois mostra
# quantas vezes apareceu valor 9
# em que posiçao o primeiro 3 aparece
# quais foram os numeros pares


cont9 = 0
numeros = []
for l in range(0,4) :
    numero = int(input('Digite um numero '))
    if numero == 9 :
        cont9 += 1
    numeros.append(numero)
tuplaNumero = tuple(numeros)
print(f'''numeros digitados :{tuplaNumero}
       Quantas vezes apareceu o numero 9 :{cont9}
       o primeiro 3 apareceu na posiçao {tuplaNumero.index(3)} 
''')
