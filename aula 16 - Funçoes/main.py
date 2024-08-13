#aula de funçoes em python

# Função que exibe um título formatado
def titulo(txt):
    print('-'*30)  # Imprime uma linha com 30 traços
    print(txt)  # Imprime o texto fornecido
    print('-'*30)  # Imprime outra linha com 30 traços

# Chamadas da função titulo com diferentes textos
titulo('    Sou foda  ')
titulo('    Melhor botlaner')
titulo('    EZ')

# Função que realiza a soma de dois valores e exibe o resultado
def soma(a, b):
    c = a + b  # Soma os dois valores e armazena em 'c'
    print(f'{a} + {b} = {c}')  # Exibe a soma formatada

# Chamadas da função soma com diferentes valores
soma(10, 20)
soma(30, 5)
soma(2, 5)

# Função que exibe uma quantidade variável de números e o tamanho da sequência
def mostra(*num):
    tam = len(num)  # Calcula o tamanho da tupla 'num'
    print(f'Recebi os números {num} e são {tam} números')  # Exibe os números recebidos e a quantidade

# Chamadas da função mostra com diferentes quantidades de argumentos
mostra(2, 5, 8)
mostra(39, 4)
mostra(2, 56, 7, 89, 12)

# Função que dobra o valor de cada elemento em uma lista
def dobra(list):
    pos = 0  # Inicializa a posição como 0
    while pos < len(list):  # Loop até que 'pos' alcance o tamanho da lista
        list[pos] *= 2  # Dobra o valor do elemento na posição 'pos'
        pos += 1  # Incrementa 'pos' para mover para o próximo elemento

# Lista de valores a serem dobrados
valores = [10, 20, 40, 58, 67]
dobra(valores)  # Chama a função dobra para alterar os valores da lista
print(valores)  # Exibe a lista de valores após serem dobrados

# Função que soma uma quantidade variável de valores e exibe o resultado
def soma(*valores):
    s = 0  # Inicializa a soma como 0
    for num in valores:  # Itera sobre cada número em 'valores'
        s += num  # Adiciona o número à soma total
    print(f'Somando os valores {valores} temos {s}')  # Exibe os valores e a soma total

# Chamadas da função soma com diferentes quantidades de argumentos
soma(4, 9)
soma(32, 32)
soma(12, 343, 54)
soma(23, 4, 6, 8)
