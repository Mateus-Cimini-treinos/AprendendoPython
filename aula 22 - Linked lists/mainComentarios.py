# Essa vai ser uma versao do codigo principal so que com comentarios para poder revisar e estudar melhor
'''
Mini Tutorial: Usando a Classe Lista

1. Criando uma lista encadeada:
   - Para criar uma nova lista encadeada, você pode passar um iterável como argumento, como uma `range`, uma lista, ou uma tupla.
   Exemplo: 
   lista = Lista(range(10))  # Cria uma lista encadeada com os valores de 0 a 9

2. Mostrando a lista:
   - Para ver os elementos da lista, basta usar a função `print()` ou converter a lista para uma string com `str()`.
   Exemplo:
   print(lista)  # Imprime a lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

3. Inserindo um elemento no final:
   - Para adicionar um novo elemento no final da lista, use o método `inserir_no_fim(valor)`.
   Exemplo:
   lista.inserir_no_fim(10)  # Adiciona o valor 10 ao final da lista

4. Inserindo um elemento em uma posição específica:
   - Para inserir um elemento em uma posição específica, use o método `inserir(posicao, valor)`.
   Exemplo:
   lista.inserir(5, 15)  # Insere o valor 15 na posição 5

5. Acessando um elemento:
   - Para acessar o valor de um elemento em uma posição específica, use o operador de índice `[]`.
   Exemplo:
   valor = lista[3]  # Acessa o valor na posição 3

6. Removendo um elemento:
   - Para remover um elemento de uma posição específica, use o operador `del` com o índice.
   Exemplo:
   del(lista[2])  # Remove o elemento na posição 2

7. Fatiando a lista:
   - Para criar uma sublista (fatia), use o operador de slice `[:]`.
   Exemplo:
   sublista = lista[2:5]  # Cria uma sublista com os elementos da posição 2 até 4

8. Verificando o comprimento da lista:
   - Para saber o número de elementos na lista, use a função `len()`.
   Exemplo:
   tamanho = len(lista)  # Retorna o número de elementos na lista
'''

class Lista:
    class No: # Classe interna para representar um nó na lista encadeada
        def __init__(self, valor, proximo=None):
            self.valor = valor  # Armazena o valor do nó
            self.proximo = proximo  # Aponta para o próximo nó na lista (ou None se for o último nó)

        def __str__(self):
            return str(self.valor)  # Retorna uma representação de string do valor do nó

    # Função para inicializar a lista encadeada, opcionalmente preenchendo-a com um iterável
    def __init__(self, interavel=None):
        self.__cabeça = None  # Inicializa a cabeça da lista (primeiro nó) como None
        self.__cauda = None  # Inicializa a cauda da lista (último nó) como None
        self.__quantidade = 0  # Inicializa a quantidade de nós na lista como 0

        if interavel is not None and hasattr(interavel, '__iter__'):
            for item in interavel:
                self.inserir_no_fim(item)  # Insere cada item do iterável no final da lista
        elif interavel is not None:
            raise TypeError(f'O objeto {type(interavel)} nao e interavel')  # Levanta um erro se o objeto não for iterável

    # Função para retornar a quantidade de elementos na lista
    def __len__(self):
        return self.__quantidade  # Retorna a quantidade de nós na lista

    # Função para retornar a representação em string da lista
    def __str__(self):
        return '['+', '.join([str(valor) for valor in self]) + ']'  # Retorna uma representação em string de toda a lista

    # Função para tornar a lista iterável
    def __iter__(self): 
        atual = self.__cabeça  # Começa a iteração a partir da cabeça da lista
        while atual is not None:
            yield atual.valor  # Retorna o valor do nó atual e move para o próximo
            atual = atual.proximo  # Avança para o próximo nó

    # Função para excluir um item da lista na posição especificada
    def __delitem__(self, posiçao):
        if posiçao < 0:
            posiçao = len(self) + posiçao  # Converte posição negativa para o índice correto

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida.')  # Levanta um erro se a posição for inválida

        self.__quantidade -= 1  # Decrementa a quantidade de nós na lista

        if posiçao == 0:
            self.__cabeça = self.__cabeça.proximo  # Remove o primeiro nó (cabeça)
            if self.__cabeça is None:
                self.__cauda = None  # Se a lista ficou vazia, atualiza a cauda para None
            return

        i = 0
        atual = self.__cabeça
        while atual.proximo is not None and i < posiçao - 1:
            atual = atual.proximo  # Itera até o nó anterior à posição a ser removida
            i += 1

        if atual.proximo == self.__cauda:
            self.__cauda = atual  # Atualiza a cauda se o nó removido for a cauda

        atual.proximo = atual.proximo.proximo  # Faz o nó anterior apontar para o nó depois do que foi removido

    # Função para acessar um item na lista pela posição ou obter uma fatia da lista
    def __getitem__(self, posiçao):
        if isinstance(posiçao, slice):
            passo = posiçao.step if posiçao.step is not None else 1  # Define o passo do slice (padrão 1)

            if passo == 0:
                raise ValueError('Passo nao pode ser igual a zero.')  # Levanta um erro se o passo for zero

            if passo > 0:
                inicio = posiçao.start if posiçao.start is not None else 0  # Define o início do slice
                fim = posiçao.stop if posiçao.stop is not None else len(self)  # Define o fim do slice
            else:
                inicio = posiçao.start if posiçao.start is not None else len(self) - 1  # Define o início para passo negativo
                fim = posiçao.stop if posiçao.stop is not None else -1  # Define o fim para passo negativo

            if inicio < 0:
                inicio = len(self) + inicio  # Converte índices negativos para positivos

            if fim < 0 and posiçao.stop is not None:
                fim = len(self) + fim  # Converte fim negativo para positivo

            fatia = Lista()  # Cria uma nova lista para armazenar a fatia
            if passo > 0:
                i = 0
                indices = range(inicio, fim, passo)  # Define os índices que serão usados no fatiamento
                it = iter(self)
                while i < fim:
                    v = next(it)
                    if i in indices:
                        fatia.inserir_no_fim(v)  # Adiciona os elementos da fatia na nova lista
                    i += 1
            else:
                for i in range(inicio, fim, passo):
                    fatia.inserir_no_fim(self[i])  # Adiciona os elementos na nova lista para passo negativo

            return fatia  # Retorna a nova lista (fatia)

        if posiçao < 0:
            posiçao = len(self) + posiçao  # Converte posição negativa para o índice correto

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')  # Levanta um erro se a posição for inválida

        atual = self.__cabeça
        for i in range(posiçao):
            atual = atual.proximo  # Busca o elemento que está na posição desejada

        return atual.valor  # Retorna o valor do elemento na posição

    # Função para inserir um novo valor no final da lista
    def inserir_no_fim(self, valor):
        novo = self.No(valor)  # Cria um novo nó com o valor fornecido
        self.__quantidade += 1  # Incrementa a quantidade de nós na lista

        if self.__cabeça is None:
            self.__cabeça = novo  # Se a lista estiver vazia, o novo nó se torna a cabeça
            self.__cauda = novo  # O novo nó também se torna a cauda
            return
        
        self.__cauda.proximo = novo  # O antigo último nó aponta para o novo nó
        self.__cauda = novo  # Atualiza a cauda para o novo nó

    # Função para inserir um novo valor em uma posição específica na lista
    def inserir(self, posiçao, valor):
        novo = self.No(valor)  # Cria um novo nó com o valor fornecido
        self.__quantidade += 1  # Incrementa a quantidade de nós na lista

        if posiçao <= 0:
            novo.proximo = self.__cabeça  # O novo nó aponta para o antigo primeiro nó
            self.__cabeça = novo  # Atualiza a cabeça para o novo nó
            return
        
        i = 0
        atual = self.__cabeça
        while atual.proximo is not None and i < posiçao - 1:
            atual = atual.proximo  # Itera até o nó anterior à posição onde o novo nó será inserido
            i += 1

        if atual.proximo is None:
            self.__cauda = novo  # Atualiza a cauda se o novo nó for inserido no final

        novo.proximo = atual.proximo  # O novo nó aponta para o próximo nó
        atual.proximo = novo  # O nó anterior aponta para o novo nó


# Teste do código

lista = Lista(range(50))  # Cria uma lista encadeada com valores de 0 a 49

print(lista)  # Imprime a lista inteira
del(lista[10])  # Remove o nó na posição 10
print(lista)  # Imprime a lista após a remoção
del(lista[0])  # Remove o nó na cabeça (posição 0)
print(lista)  # Imprime a lista após a remoção
del(lista[1])  # Remove o nó na posição 1
print(lista)  # Imprime a lista após a remoção
del(lista[-1])  # Remove o nó na cauda (última posição)
print(lista)  # Imprime a lista após a remoção
