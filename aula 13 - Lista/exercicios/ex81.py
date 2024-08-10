#crie um programa que vai ler numeros do usuario enquanto ele quiser e no final mostrar
# quantos numeros foram digitados
#ordem ordenada de forma decrecente
# se o valor 5 foi digitado

num = []
while True:
    num.append(int(input('Adicione um valor à lista: ')))
    continuar = input('Quer adicionar mais números? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

quantidade = len(num)

print(f'Os números adicionados são: {num}')
print(f'Você adicionou {quantidade} números')
print(f'Seus números em ordem decrescente: {sorted(num, reverse=True)}')

if 5 in num:
    print('O número 5 está na lista')
    posicao = num.index(5)
    print(f'E o número 5 está na posição {posicao}')
else:
    print('Não há 5 na lista')
