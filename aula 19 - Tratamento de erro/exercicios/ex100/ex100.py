from lib.arquivo import arqExiste, cadastrar
from lib.inteface import *
from lib.arquivo import *
from time import sleep



arq = 'aula 2 Python/aula 19 - Tratamento de erro/exercicios/ex100/mateus.txt'


if not arqExiste(arq):
    criarArq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
    if resposta == 1 : 
        #opçao de listar conteudo do arquivo
        lerArq(arq)
    elif resposta == 2 : 
        #opçao de cadastrar novas pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3 : 
        #opçao sair do sistema
        cabeçalho('Saindo do Sistema')
        break
    else:
        print('\033[31mERRO: digite um opçao valida\033[m')
    sleep(1)