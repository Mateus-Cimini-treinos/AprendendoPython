#aula sobre lista 
# Definindo a lista inicial e substituindo o elemento no índice 2
num = [1, 4, 7, 2, 4]
print(num)

# Alterando o valor no índice 2
num[2] = 10
print(num)

# Adicionando um novo elemento ao final da lista
num.append(22)
print(num)

# Ordenando a lista em ordem crescente
num.sort()
print(num)

# Revertendo a ordem da lista
num.reverse()
print(num)

# Exibindo a quantidade de elementos na lista
print(f'Essa lista tem {len(num)} numeros')

# Inserindo um elemento na posição 4
num.insert(4, 50)
print(num)

# Removendo o último elemento da lista
num.pop()
print(num)

# Removendo o elemento na posição 1
num.pop(1)
print(num)

# Removendo a primeira ocorrência do número 4 na lista
num.remove(4)
print(num)


# Verificando e removendo um número específico
num.insert(2, 5)
print(num)

# Verificando se o número 5 está na lista e removendo se estiver
if 5 in num:
    num.remove(5)
else:
    print('nao tem 5')
print(num)


# Adicionando valores em uma lista vazia e exibindo os valores com um loop
valores = []
valores.append(2)
valores.append(8)
valores.append(5)

for v in valores:
    print(f' {v}...', end=' ')

# Usando enumerate para mostrar a posição e o valor de cada item na lista
for c, v in enumerate(valores):
    print(f'\nna posiçao {c} encontrei {v}')


# Recebendo valores do usuário e adicionando-os a uma lista
inputvalor = []
for cont in range(0, 5):
    inputvalor.append(int(input('Digite um valor ')))
print(inputvalor)


# Demonstrando cópias de listas: cópia direta vs cópia de fatia
a = [2, 4, 5, 8]
b = a  # b é uma referência para a mesma lista que a
print(a)
print(b)

# Modificando um elemento em b também altera a lista a
b[2] = 8
print(a)
print(b)

# Fazendo uma cópia independente da lista a
c = a[:]
c[2] = 9  # Alterações em c não afetam a ou b
print(a)
print(b)
print(c)

'''
----------------------BONUS----------------------BONUS----------------------BONUS----------------------BONUS----------------------BONUS---------
'''

# Criando uma lista simples com cinco elementos
minha_lista = [1, 2, 3, 4, 5]

# Acessando o primeiro e o último elemento da lista
primeiro_elemento = minha_lista[0]  # Retorna 1
ultimo_elemento = minha_lista[-1]   # Retorna 5

# Modificando o primeiro elemento da lista
minha_lista[0] = 10  # Agora, minha_lista é [10, 2, 3, 4, 5]

# Adicionando um novo elemento ao final da lista
minha_lista.append(6)  # Agora, minha_lista é [10, 2, 3, 4, 5, 6]

# Inserindo um elemento na terceira posição da lista
minha_lista.insert(2, 20)  # Agora, minha_lista é [10, 2, 20, 3, 4, 5, 6]

# Removendo a primeira ocorrência do número 20
minha_lista.remove(20)  # Agora, minha_lista é [10, 2, 3, 4, 5, 6]

# Removendo o segundo elemento da lista e armazenando-o em uma variável
elemento_removido = minha_lista.pop(1)  # Retorna 2, e minha_lista é [10, 3, 4, 5, 6]

# Removendo o primeiro elemento da lista usando o comando 'del'
del minha_lista[0]  # Agora, minha_lista é [3, 4, 5, 6]

# Criando uma sublista que inclui o segundo e o terceiro elementos da lista original
sublista = minha_lista[1:3]  # Retorna [4, 5]

# Contando o número de elementos na lista
tamanho = len(minha_lista)  # Retorna 4

# Ordenando os elementos da lista em ordem crescente
minha_lista.sort()  # Agora, minha_lista é [3, 4, 5, 6]

# Invertendo a ordem dos elementos na lista
minha_lista.reverse()  # Agora, minha_lista é [6, 5, 4, 3]

# Criando uma nova lista de quadrados de números de 0 a 4 usando list comprehension
quadrados = [x**2 for x in range(5)]  # Cria [0, 1, 4, 9, 16]

# Exemplo de uso com uma lista de frutas
frutas = ['maçã', 'banana', 'laranja']
frutas.append('uva')  # Adiciona 'uva'
frutas.remove('banana')  # Remove 'banana'
print(frutas)  # Exibe ['maçã', 'laranja', 'uva']
