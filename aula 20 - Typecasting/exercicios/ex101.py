#Peça ao usuário para digitar dois números. Converta os números para inteiros e exiba a soma deles.


n1 = input('Digite um número: ')
n1 = n1.replace(',', '.')
n1 = float(n1)


n2 = input('Digite outro número: ')
n2 = n2.replace(',', '.')
n2 = float(n2)

resultado = n1 + n2

print(f'A soma entre {n1} e {n2} é {resultado}')
