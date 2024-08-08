# ceie um codigo que recebe um numero de 0 a 9999 e diz
# 1 quantas unidades
# 2 quantas dezenas
# 3 quantas cetenas
# 4 quantas milhares 

num = str(input('Digite um numero entre 0 a 9999 >> '))

num = num.zfill(4)

character = list(num)
print('Analizando o numero {}...'.format(num))
print('Seu numero tem',character[3],' unidades')
print('Seu numero tem',character[2],' dezenas')
print('Seu numero tem',character[1],' centenas')
print('Seu numero tem',character[0],' milhares')