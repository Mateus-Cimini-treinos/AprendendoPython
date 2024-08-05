# crie um programa que recebe um nome e fala qual e o ultimo nome e o primeiro

name = str(input('Qual o seu nome completo?'))

nameSplit = name.split()

lastName = nameSplit[-1]


print('Analizando o nome...')
print('O primeiro nome é:', nameSplit[0])
print('O ultimo nome é:', lastName)