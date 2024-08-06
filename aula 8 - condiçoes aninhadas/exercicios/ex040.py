'''crie um programa que recebe 2 notas do aluno e da uma resposta se a nota for

menor que 5 = reprovado
entre 5.1 e 6.9 = recuperaçao
maior que 7 = aprovado

'''

grade1 = float(input('Valor da primeira nota '))
grade2 = float(input('Valor da segunda nota '))

average = (grade1 + grade2) / 2

if average <= 5.0 :
    print('Sua media foi de {:.1f} e vc esta reprovado pq e menor que 5.0'.format(average))
elif average > 5.0 and average <= 6.9 :
    print('Sua media foi de {:.1f} e vc esta de recuperaçao pq a nota esta entre 5.1 e 6.9'.format(average))
else:
    print('Sua media foi de {:.1f} e vc esta aprovado pq e superior a 7.0'.format(average))