# Programa para registrar nomes, notas, e calcular a média de cada aluno.
# Permite visualizar o boletim com nome e média de cada aluno, e visualizar as notas também.

turma = []  

while True:
    aluno = []  
    notas = []  
    nome = str(input('Qual o nome do aluno? '))
    aluno.append(nome) 

    nota1 = float(input('Adicione a nota 1: '))
    nota2 = float(input('Adicione a nota 2: '))
    notas.append(nota1)
    notas.append(nota2)

    media = sum(notas) / 2  
    aluno.append(media)  

    aluno.append(notas[:])  
    turma.append(aluno[:])  

    continuar = input('Quer adicionar mais alunos? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Resposta inválida! Digite S para sim ou N para não.')


print(f'''
+------------+-------------------+-------+
| N° Aluno   | Nome              | Média |
+------------+-------------------+-------+''')

for i, aluno in enumerate(turma):
    print(f'| {i+1:<10} | {aluno[0]:<17} | {aluno[1]:>5.2f} |')
    print('+------------+-------------------+-------+')


while True:
    ver_notas = input('\nDeseja ver as notas de algum aluno? [S/N] ').strip().upper()
    if ver_notas == 'N':
        break
    elif ver_notas == 'S':
        num_aluno = int(input('Digite o número do aluno: ')) - 1
        if 0 <= num_aluno < len(turma):
            print(f'As notas de {turma[num_aluno][0]} são: {turma[num_aluno][2]}')
        else:
            print('Número de aluno inválido!')
    else:
        print('Resposta inválida! Digite S para sim ou N para não.')
