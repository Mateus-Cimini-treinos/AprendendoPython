#crie um programa que recebe numeros ate dizer nao e salva em uma lista no final ele mostar uma lista apenas com pares e outra com impares e uma com todos os numeros


num = []
while True:
    num.append(int(input('Adicione um valor à lista: ')))
    continuar = input('Quer adicionar mais números? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

pares = [n for n in num if n % 2 == 0 ]
impares = [n for n in num if n % 2 != 0]
print(f'os numeros adicionados sao: {num}')
print(f'os numeros pares adicionados sao: {pares}')
print(f'os numeros impares adicionados sao: {impares}')