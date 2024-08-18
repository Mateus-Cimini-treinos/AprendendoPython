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
    class No:
        def __init__(self, valor, proximo=None):  # Construtor da classe interna No
            self.valor = valor  # Armazena o valor do nó
            self.proximo = proximo  # Armazena a referência ao próximo nó

        def __str__(self):  # Método para representar o nó como string
            return str(self.valor)

    def __init__(self, interavel=None):  # Construtor da classe Lista
        self.__cabeça = None  # Inicia a cabeça da lista como None
        self.__cauda = None  # Inicia a cauda da lista como None
        self.__quantidade = 0  # Inicia o contador de elementos na lista

        # Se um objeto iterável for fornecido, popula a lista com seus elementos
        if interavel is not None and hasattr(interavel, '__iter__'):
            for item in interavel:
                self.inserir_no_fim(item)
        elif interavel is not None:
            raise TypeError(f'O objeto {type(interavel)} nao e interavel')

    def __len__(self):  # Método para obter o tamanho da lista
        return self.__quantidade

    def __str__(self):  # Método para representar a lista como string
        return '['+', '.join([str(valor) for valor in self]) + ']'

    def __iter__(self):  # Método para tornar a lista iterável
        atual = self.__cabeça  # Começa a iteração a partir da cabeça
        while atual is not None:
            yield atual.valor  # Retorna o valor do nó atual
            atual = atual.proximo  # Move para o próximo nó

    # Função para definir um valor em uma posição específica da lista
    def __setitem__(self, posiçao, valor):
        if posiçao < 0:
            posiçao = len(self) + posiçao  # Ajusta a posição se for negativa

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')  # Lança erro se a posição for inválida
        
        atual = self.__cabeça  # Começa a buscar a partir da cabeça
        for i in range(posiçao):
            atual = atual.proximo  # Navega até o nó na posição desejada

        atual.valor = valor  # Define o novo valor para o nó na posição

    # Função para excluir um item da lista em uma posição específica
    def __delitem__(self, posiçao):
        if posiçao < 0:
            posiçao = len(self) + posiçao  # Ajusta a posição se for negativa
        
        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida.')
        
        self.__quantidade -= 1

        # Removendo da cabeça
        if posiçao == 0:
            self.__cabeça = self.__cabeça.proximo
            if self.__cabeça is None:
                self.__cauda = None
            return

        i = 0
        atual = self.__cabeça
        # Buscando elemento anterior à posição que queremos remover
        while atual.proximo is not None and i < posiçao - 1:
            atual = atual.proximo
            i += 1
        
        # Removendo a cauda, se necessário
        if atual.proximo == self.__cauda:
            self.__cauda = atual

        # Removendo o elemento desejado
        atual.proximo = atual.proximo.proximo

    # Função para acessar um item em uma posição específica ou uma fatia da lista
    def __getitem__(self, posiçao):
        if isinstance(posiçao, slice):
            passo = posiçao.step if posiçao.step is not None else 1

            if passo == 0:
                raise ValueError('Passo nao pode ser igual a zero.')

            if passo > 0:
                inicio = posiçao.start if posiçao.start is not None else 0
                fim = posiçao.stop if posiçao.stop is not None else len(self)
            else:
                inicio = posiçao.start if posiçao.start is not None else len(self) - 1
                fim = posiçao.stop if posiçao.stop is not None else -1

            if inicio < 0:
                inicio = len(self) + inicio

            if fim < 0 and posiçao.stop is not None:
                fim = len(self) + fim
            
            fatia = Lista()
            if passo > 0:
                i = 0
                indices = range(inicio, fim, passo)
                it = iter(self)
                while i < fim:
                    v = next(it)
                    if i in indices:
                        fatia.inserir_no_fim(v)
                    i += 1
            else:  # Passo negativo, usa __getitem__
                for i in range(inicio, fim, passo):
                    fatia.inserir_no_fim(self[i])

            return fatia

        if posiçao < 0:
            posiçao = len(self) + posiçao

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')

        atual = self.__cabeça  # Busca o elemento na posição desejada
        for i in range(posiçao):
            atual = atual.proximo

        return atual.valor  # Retorna o valor do nó encontrado

    # Função para inserir um item no final da lista
    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # Se a lista está vazia
        if self.__cabeça is None:
            self.__cabeça = novo
            self.__cauda = novo
            return
        
        self.__cauda.proximo = novo  # Adiciona o novo nó após o último nó atual
        self.__cauda = novo  # Atualiza a cauda para ser o novo nó

    # Função para inserir um item em uma posição específica da lista
    def inserir(self, posiçao, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # Inserir na cabeça (primeira posição)
        if posiçao <= 0:
            novo.proximo = self.__cabeça
            self.__cabeça = novo
            return
        
        i = 0
        atual = self.__cabeça
        # Buscando o elemento anterior à posição onde queremos inserir
        while atual.proximo is not None and i < posiçao - 1:
            atual = atual.proximo
            i += 1

        if atual.proximo is None:  # Inserir na cauda (última posição)
            self.__cauda = novo

        novo.proximo = atual.proximo  # Conecta o novo nó à lista
        atual.proximo = novo  # Atualiza a ligação do nó anterior para o novo nó

# Exemplo de uso:
lista = Lista(range(50))

print(lista)  # Exibe a lista completa
del(lista[10])  # Deleta o item na posição 10
print(lista)
del(lista[0])  # Deleta o primeiro item (posição 0)
print(lista)
del(lista[1])  # Deleta o item na posição 1
print(lista)
del(lista[-1])  # Deleta o último item (posição -1)
print(lista)
lista[-1] = 'Mateus'  # Altera o último item para 'Mateus'
print(lista)
