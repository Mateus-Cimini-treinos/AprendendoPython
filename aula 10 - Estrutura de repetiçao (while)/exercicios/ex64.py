# crie um programa que recebe numeros ate que a resposta seja 999 e no final mostre quantos numeros foi digitados e a soma entre todos numeros digitados

num = soma = 0
cont = 1
while num != 999 :
    num = int(input('qual vai ser o numero da casa {}?? '.format(cont)))
    ultimo = num
    if ultimo == 999 :
        soma -= 999
        cont -= 2
    cont += 1
    soma += num
print("voce digitou {} numeros a soma de todos os numeros e de : {}".format(cont,soma))
