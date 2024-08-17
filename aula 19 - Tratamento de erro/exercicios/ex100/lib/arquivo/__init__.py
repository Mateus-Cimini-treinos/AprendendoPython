from lib.inteface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criaçao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('houve um erro ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever o arquivo')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()