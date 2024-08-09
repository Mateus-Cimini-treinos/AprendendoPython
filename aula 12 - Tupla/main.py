# Aula de Tupla


# Definindo uma tupla com rotas de jogo
rotas = ('baron', 'jungle', 'mid', 'adc', 'suporte')

# Acessando elementos específicos da tupla
print(rotas[-5])  # Primeiro elemento
print(rotas[1:3]) # Elementos do segundo ao terceiro
print(rotas[2:])  # Elementos a partir do terceiro até o final
print(rotas[:2])  # Elementos do início até o segundo
print(rotas[-2:]) # Últimos dois elementos da tupla

# Iterando sobre a tupla usando for
for l in rotas:
    print(f'Eu jogo de {l}')

# Iterando sobre a tupla usando range e len
for cont in range(0, len(rotas)):
    print(rotas[cont])

# Iterando sobre a tupla usando enumerate para obter o índice e o valor
for pos, lane in enumerate(rotas):
    print(lane, pos)

# Exibindo a tupla em ordem alfabética sem alterar a tupla original
print(sorted(rotas))
# Exibindo a tupla original
print(rotas)


# Operações com tuplas
a = (1, 4, 6)
b = (2, 4, 8, 10)

# Concatenando tuplas
c = a + b  # Primeiro a seguido de b
d = b + a  # Primeiro b seguido de a

# Exibindo as tuplas
print(a)
print(b)
print(c)
print(d)

# Outras operações
print(len(c))        # Quantidade de elementos na tupla c
print(c.count(4))    # Quantas vezes o número 4 aparece na tupla c
print(c.count(6))    # Quantas vezes o número 6 aparece na tupla c
print(c.index(4))    # Posição da primeira ocorrência do número 4 em c


# Trabalhando com diferentes tipos de dados em tuplas
mateus = ('gostoso', 1.66, 'lindo', True)
print(mateus)

# Deletando uma tupla
del(mateus)

# Isso causará um erro, pois a tupla 'mateus' foi deletada
# print(mateus)  # Descomente para ver o erro


# Outros exemplos de tuplas (adicionei aqui)

# Criando tuplas diretamente com variáveis
x, y, z = (10, 20, 30)
print(x, y, z)

# Tupla com um único elemento (note a vírgula)
single_element = (42,)
print(single_element)

# Verificando se um elemento está na tupla
print(4 in a)  # Retorna True, pois 4 está na tupla a
print(7 not in b)  # Retorna True, pois 7 não está na tupla b

# Concatenando múltiplas tuplas
combined = a + b + (9, 7)
print(combined)
