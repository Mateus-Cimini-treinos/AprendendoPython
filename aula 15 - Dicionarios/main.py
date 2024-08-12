#aula de python sobre dicionarios

# Criação de um dicionário com informações sobre uma pessoa
pessoa = {'nome':'Mateus', 'idade':18, 'sexo': 'M', 'casado': False}

# Acessando e imprimindo valores específicos do dicionário usando as chaves
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['sexo'])
print(pessoa['casado'])

# Usando f-string para formatar uma string que inclui valores do dicionário
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos!')

# Imprimindo todas as chaves, valores e itens (pares chave-valor) do dicionário
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

# Iterando sobre as chaves do dicionário e imprimindo cada uma
for k in pessoa.keys() :
    print(k)

# Iterando sobre os valores do dicionário e imprimindo cada um
for v in pessoa.values() :
    print(v)

# Iterando sobre os itens do dicionário (chave e valor) e imprimindo-os
for k, v in pessoa.items() :
    print(f'{k} = {v}')

# Removendo a chave 'casado' do dicionário
del pessoa['casado']
print(pessoa)

# Modificando o valor da chave 'idade'
pessoa['idade'] = 19
print(pessoa)

# Adicionando uma nova chave 'peso' ao dicionário
pessoa['peso'] = 55.5
print(pessoa)


# Trabalhando com listas de dicionários
animes = []  # Criando uma lista vazia para armazenar os dicionários de animes

# Criando dicionários com informações sobre animes
anime1 = {'nome':'Naruto', 'ano': 2000, 'tema':'shounen', 'protagonista':'Naruto'}
anime2 = {'nome':'Dargon Ball', 'ano': 1998, 'tema':'shounen', 'protagonista':'Goku'}

# Imprimindo a lista e os dicionários criados
print(animes)
print(anime1)
print(anime2)

# Adicionando os dicionários à lista 'animes'
animes.append(anime1)
print(animes)
animes.append(anime2)
print(animes)

# Acessando e imprimindo os dicionários dentro da lista 'animes'
print(animes[0])
print(animes[1])

# Acessando e imprimindo valores específicos dos dicionários dentro da lista
print(animes[0]['ano'])
print(animes[1]['protagonista'])

# Usando um loop para criar dicionários e adicioná-los a uma lista
anime = {}  # Criando um dicionário vazio
animess = []  # Criando uma lista vazia para armazenar os dicionários
for c in range(0, 3):  # Loop que se repete 3 vezes
    # Adicionando dados ao dicionário 'anime'
    anime['nome'] = str(input('Nome do anime: '))
    anime['data de lançamento'] = int(input('Qual a data de lançamento: '))
    # Usando copy() para garantir que uma cópia do dicionário seja adicionada à lista
    animess.append(anime.copy())

# Iterando sobre a lista de dicionários e imprimindo os valores de cada chave
for e in animess:
    for n, d in e.items():
        print(f'O campo {n} tem o valor {d}')
