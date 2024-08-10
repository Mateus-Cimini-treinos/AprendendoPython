#faça um programa que recebe nome e peso de varias pessoas e salva em uma lista e no final mostre
#quantas pessoas foram cadastradas
#as pessoas mais pesadas
#as pessoas mais leves

pessoa = []
galera = []
while True:
    pessoa.append(str(input('Nome:')))
    pessoa.append(int(input('Peso:')))
    galera.append(pessoa[:])
    pessoa.clear()
    continuar = input('Quer adicionar mais pessoas? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

quantos = len(galera)

mais_leves = [galera[0]]
mais_pesados = [galera[0]]

for pessoa in galera[1:]:
    if pessoa[1] < mais_leves[0][1]:
        mais_leves = [pessoa]
    elif pessoa[1] == mais_leves[0][1]:
        mais_leves.append(pessoa)

    if pessoa[1] > mais_pesados[0][1]:
        mais_pesados = [pessoa]
    elif pessoa[1] == mais_pesados[0][1]:
        mais_pesados.append(pessoa)

print(f'Foram cadastradas {quantos} pessoas')

print('As pessoas mais leves são:')
for leve in mais_leves:
    print(f'{leve[0]} com {leve[1]} kg')

print('As pessoas mais pesadas são:')
for pesado in mais_pesados:
    print(f'{pesado[0]} com {pesado[1]} kg')


