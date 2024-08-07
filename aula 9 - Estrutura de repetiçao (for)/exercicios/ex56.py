somaidade = 0
mediaidade = 0
maiorIdadeHomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1, 5):
    print('--------- {}ª PESSOA --------'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()  # Corrigido para aplicar strip e upper
    
    somaidade += idade
    
    if sexo == 'M':
        if p == 1 or idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomevelho = nome
    elif sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print('A média das idades é {:.2f}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
