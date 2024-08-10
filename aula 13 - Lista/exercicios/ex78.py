#crie um programa que recebe 5 valores e guarde em uma lista e depois mostre
#qual o maior e menor e suas posiçoes na lista


numList = []
for cont in range(0, 5) :
    numList.append(int(input('Adicione um numero a lista  ')))
    maior = max(numList)
    menor = min(numList)
print(f'O menor número adicionado é {menor} e está na(s) posição(ões): ', end='')
for i, n in enumerate(numList):
    if n == menor:
        print(f'{i}', end=' ')
        
print(f'\nO maior número adicionado é {maior} e está na(s) posição(ões): ', end='')
for i, n in enumerate(numList):
    if n == maior:
        print(f'{i}', end=' ')
