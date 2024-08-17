# Peça ao usuário para digitar seu nome e sua idade. Converta a idade para inteiro, some 5 anos e exiba uma mensagem dizendo quantos anos o usuário terá daqui a 5 anos.

name = input('Qual o seu nome? ')
years = input('Qual a sua idade? ')

yearsInt = int(years)

yearsInt += 5

years = str(yearsInt)

print(f'Seu nome é {name} e sua idade acresentando 5 anos é {years} anos')