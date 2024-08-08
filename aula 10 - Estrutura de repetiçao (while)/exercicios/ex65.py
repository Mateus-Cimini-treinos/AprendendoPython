# crie um programa que  recebe numeros inteiros ate que responda N
#no  final mostre a media entre todos
# qual o maior
# qual o menor

num = cont = media = soma = 0
menor = maior =  None
resposta = 'S'
while resposta != 'N' :
    num = int(input('Digite um valor: '))
    soma += num
    ultimo = num 
    if cont == 0 :
        menor = maior = num
    else :
        if num > maior :
            maior = num
        if num < menor :
            menor = ultimo
    cont +=1 
    media = soma / cont
    resposta = str(input('Quer continuar? [S/N]  ')).upper()
print('Voce disse {} numeros, e a media aritimetica e de {},o ultimo numero foi {}, o maior e {}, e o menor e {}'.format(cont,media,ultimo,maior,menor))


    