#crie um programa que recebe valores ate o usuario dizer nao, e esses valores sao cadastrados em uma lista e se o numero e repetido ele nao e salvo, e no final mostra os valores em ordem cressente


continuar = 'S'
num = []
numUnicos = []

while True:
    num.append(int(input('Adicione um valor à lista: ')))
    continuar = input('Quer adicionar mais números? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

for n in num:
    if n not in numUnicos:
        numUnicos.append(n)

print(f'A lista principal é {num}, mas a lista com os repetidos removidos é {numUnicos}.')
