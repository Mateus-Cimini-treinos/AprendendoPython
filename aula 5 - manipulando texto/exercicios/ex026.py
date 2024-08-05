#crie um programa que recebe uma frase e diz
# 1 quantas vezes a letra A aparece
# 2 em que posiçao ela aparece pela primeira vez
# 3 em que posiçao ela aparece pela ultima vez

text = str(input('Digite uma frase '))

textLower = text.lower()

#1
heHasA = textLower.count('a')

#2
fistPositionA = textLower.find('a')

#3
lastPositionA = textLower.rfind('a')

print('Analisando sua frase...')
print('Ela tem {} letras "a"'.format(heHasA))
print('A posiçao da primeira letra "a" é: {}'.format(fistPositionA))
print('A posiçao da ultima letra "a" é: {}'.format(lastPositionA))