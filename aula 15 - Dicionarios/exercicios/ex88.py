#crie um programa que recebe nome,sexo e idade de pessoas !
#guarda os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista!
#no final mostra
#quantas pessoas foram cadastradas !
#a media de idade do grupo é !
#uma lista com todas as mulheres !
#uma lista com todas as pessoas com idade acima da media

galera = []
pessoa = {}
somaIdade = 0
mulheres = []
pessoaAcima = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if pessoa['sexo'] == 'F' or pessoa['sexo'] == 'M':
            break
        elif pessoa['sexo'] != 'F' or pessoa['sexo'] != 'M':
            print('resposta invalida digite F para feminino ou M para masculino ')

    if pessoa['sexo'] == 'F' :
        mulheres.append(pessoa['nome'])

    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    



    galera.append(pessoa.copy())
    quantidadePessoas = len(galera)
    mediaIdades = somaIdade / quantidadePessoas

    if pessoa['idade'] > mediaIdades :
        pessoaAcima.append(pessoa.copy())

    while True:
        continuar = input('Quer adicionar mais alunos? [S/N] ').strip().upper()
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
        else:
            print('Resposta inválida! Digite S para sim ou N para não.')
    if continuar == 'N':
        break   



nomeMulheres = ' , '.join(mulheres)



print(f'''
Foram cadastradas {quantidadePessoas} pessoas!
A media de idade é: {mediaIdades}
Todas as mulheres adicionadas são {nomeMulheres}
      ''')
print('Pessoas cokm idades acima da media')
for e in pessoaAcima :
    for c, v in e.items():
       
        print(f'''o {c} é: {v} ''')

