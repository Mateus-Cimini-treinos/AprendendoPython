# crie um codigo que recebe um nome completo e fala 
# 1 nome todo em maisuculo
# 2 nome todo em minusculo
# 3 quantas letras ao todo sem contar espaços
# 4 quantas letras tem o primeiro nome

name = str(input('Digite seu nome completo >  '))
#1
upper = name.upper()

#2
lower = name.lower()


listName = name.split()

#3
joining = ''.join(listName)
length = len(joining)

#4
fistName = listName[0]
lengthFistName = len(fistName)


print('Analisando seu nome...')
print('O nome é: {}\nEm maiusculo fica: {}\nEm minusculo fica: {}\nQuantidade de caracteres sem contar espaço é: {}\nO primeiro nome tem {} Letras'.format(name,upper,lower, length, lengthFistName))