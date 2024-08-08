# crie um programa que registra a idade e o sexo de pessoas
# ate que a pergunta seja respondida com nao
# vai mostrar 
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres de menos de 20 anos foram cadastradas

maiorIdade = 0
masculino = 0
mulherMenos = 0

print('---REGISTRADOR DE PESSOAS---')

while True:
    idade = int(input('Qual a idade da pessoa? '))
    sexo = input('Qual o sexo da pessoa [M/f]? ').strip().upper()
    
    if idade >= 18:
        maiorIdade += 1
        
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F' and idade <= 20:
        mulherMenos += 1
    
    continuar = input('Quer adicionar mais pessoas? [S/N] ').strip().upper()
    
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')

print('--PESSOAS CADASTRADAS--')
print(f'Você adicionou {maiorIdade} pessoas com mais de 18 anos')
print(f'No total foram adicionadas {masculino} pessoas do sexo masculino')
print(f'E tem {mulherMenos} mulheres com menos de 20 anos')
print('Fim')
