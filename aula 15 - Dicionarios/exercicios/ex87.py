##crie um programa que rece o nome e a media do aluno e vai guarda no dicionario e no final diz o nome, a media e se ele foi aprovado ou reprovado

aluno = {}
aprovado = None
for c in range(0,1):
    aluno['nome'] = str(input('nome do aluno '))
    aluno['media'] = float(input('media do aluno '))
   

print(f'O nome do aluno é: {aluno['nome']} a media dele foi: {aluno['media']}')
if aluno['media'] >= 7.5 :
    aprovado = True
else: aprovado == False
if aprovado == True :
    print('ele esta aprovado')
else :
    print('ele esta reprovado')