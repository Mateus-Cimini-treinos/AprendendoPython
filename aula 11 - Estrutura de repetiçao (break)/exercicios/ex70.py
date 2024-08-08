# crie um programa que aceitanome e preço de produtos ate dizer nao no final vai mostrar
#valor total gasto
#quantos produtos custao mais de 1000 reais
# nome do produto mais barato

valorTotal = maisdeMil = maisBarato = cont = 0
ultimonome = ''
ultimopreço = float('inf')  

print('---REGISTRADOR DE PRODUTO---')

while True:
    nome = input('Qual o nome do produto? ').strip()
    preço = float(input('Qual o preço? R$'))  
    
    valorTotal += preço 

    if preço > 1000:
        maisdeMil += 1

    if cont == 0:
        ultimopreço = preço
        maisBarato = nome
    else:
        if preço < ultimopreço:
            ultimopreço = preço
            maisBarato = nome

    cont += 1 

    continuar = input('Quer adicionar mais produtos? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

print('--INFORMAÇÕES--')
print(f'Total da compra é de R${valorTotal:.2f}')
print(f'No total foram adicionados {maisdeMil} produtos que custam mais de R$1.000')
print(f'O produto mais barato é: {maisBarato} com o preço de R${ultimopreço:.2f}')
print('Fim')

