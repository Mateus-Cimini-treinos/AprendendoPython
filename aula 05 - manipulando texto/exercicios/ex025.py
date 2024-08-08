#crie um programa que le o nome de uma pessoa e diz se termina com 'Silva'

name = str(input('Qual o seu nome completo >> '))

nameUpper = name.upper()

finalName = nameUpper[5:]

check = 'SILVA' in finalName


if(check == True): print('Seu ultimo nome e Silva')
else :  print('Seu ultimo nome nao e Silva')