# crie um programa que recebe numeros ate que a resposta seja 999 e no final mostre quantos numeros foi digitados e a soma entre todos numeros digitados
num = soma = 0
cont = 1
while True :
    num = int(input(f'qual vai ser o numero da casa {cont}?? (se quiser sair digite "999") '))
    ultimo = num
    if ultimo == 999 :
        cont -= 1
        break
    cont += 1
    soma += num
print(f"voce digitou {cont} numeros a soma de todos os numeros e de : {soma}")