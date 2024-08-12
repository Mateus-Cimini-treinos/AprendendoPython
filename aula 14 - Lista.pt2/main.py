# Definindo uma lista chamada 'galera' que contém outras listas dentro dela.
# Cada lista interna representa uma pessoa, com o nome e a idade.
galera = [['Mateus', 18], ['Maria', 20], ['Joao', 23]]
print(galera)  # Exibe a lista completa.

# Iterando sobre cada elemento da lista 'galera'.
# Cada elemento é uma lista com o nome e a idade de uma pessoa.
for p in galera:
    print(p)  # Exibe a lista completa para cada pessoa (ex: ['Mateus', 18]).
    print(p[0])  # Exibe o nome da pessoa (primeiro elemento da lista).
    print(p[1])  # Exibe a idade da pessoa (segundo elemento da lista).
    print(f'o {p[0]} tem {p[1]} anos de idade')  # Exibe uma frase formatada com o nome e a idade.

# Iniciando uma nova lista 'galera1' vazia, que armazenará os dados das pessoas.
galera1 = []
# Iniciando uma lista 'dados' vazia que será usada para armazenar temporariamente os dados de cada pessoa.
dados = []
# Iniciando contadores para contar o número de pessoas maiores e menores de idade.
totmaior = totmenor = 0

# Loop que executa 4 vezes, permitindo que o usuário insira o nome e a idade de 4 pessoas.
for c in range(0, 4):
    dados.append(str(input('Digite o nome: ')))  # Adiciona o nome à lista 'dados'.
    dados.append(int(input('Digite a idade: ')))  # Adiciona a idade à lista 'dados'.
    galera1.append(dados[:])  # Adiciona uma cópia da lista 'dados' à lista 'galera1'.
    dados.clear()  # Limpa a lista 'dados' para que possa ser usada para a próxima pessoa.

print(galera1)  # Exibe a lista completa 'galera1', que agora contém os dados das 4 pessoas.

# Itera sobre cada elemento da lista 'galera1'.
# Cada elemento é uma lista com o nome e a idade de uma pessoa.
for p in galera1:
    if p[1] >= 18:  # Verifica se a idade da pessoa é maior ou igual a 18 anos.
        print(f'{p[0]} é maior de idade')  # Exibe que a pessoa é maior de idade.
        totmaior += 1  # Incrementa o contador de maiores de idade.
    else:
        print(f'{p[0]} é menor de idade')  # Exibe que a pessoa é menor de idade.
        totmenor += 1  # Incrementa o contador de menores de idade.

# Exibe a quantidade total de maiores e menores de idade.
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
