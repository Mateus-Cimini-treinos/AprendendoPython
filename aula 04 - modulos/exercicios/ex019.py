# crie um algoritimo que recebe nomes e printa um aleatorio
import random

students = input("Nome dos alunos separados por espaços ")

list = students.split()

drawn = random.choice(list)

print('O aluno sorteado foi: {}!'.format(drawn))