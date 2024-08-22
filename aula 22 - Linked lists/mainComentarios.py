# Essa vai ser uma versao do codigo principal so que com comentarios para poder revisar e estudar melhor
'''
Mini Tutorial para Lista Encadeada (Linked List)

1. Criação de uma Lista Encadeada:
   - `lista = Lista(['Mateus', 'Felipe', 'Lucas'])`
     Cria uma lista encadeada com os elementos fornecidos.

2. Inserir um elemento no final:
   - `lista.inserir_no_fim('Maria')`
     Adiciona o valor 'Maria' ao final da lista.

3. Inserir um elemento em uma posição específica:
   - `lista.inserir(1, 'Joao')`
     Insere o valor 'Joao' na posição 1 da lista.

4. Acessar um elemento por índice:
   - `valor = lista[2]`
     Retorna o valor na posição 2 da lista.

5. Modificar um elemento em uma posição específica:
   - `lista[1] = 'Felicia'`
     Substitui o valor na posição 1 por 'Felicia'.

6. Remover um elemento por índice:
   - `del lista[3]`
     Remove o valor na posição 3 da lista.

7. Remover um elemento por valor:
   - `lista.remover('Lucas')`
     Encontra e remove a primeira ocorrência de 'Lucas' na lista.

8. Obter o índice de um valor:
   - `indice = lista.indice('Maria')`
     Retorna o índice da primeira ocorrência de 'Maria' na lista.

9. Contar quantas vezes um valor aparece:
   - `quantidade = lista.contar('Maria')`
     Retorna o número de vezes que 'Maria' aparece na lista.

10. Reverter a lista:
    - `lista.reverter()`
      Reverte a ordem dos elementos na lista.

11. Copiar a lista:
    - `copia = lista.copiar()`
      Retorna uma cópia da lista original.

12. Limpar a lista:
    - `lista.limpar()`
      Remove todos os elementos da lista.

13. Remover e retornar o último elemento:
    - `ultimo = lista.pop()`
      Remove e retorna o último elemento da lista.

14. Obter uma fatia (slice) da lista:
    - `sublista = lista[1:4]`
      Retorna uma nova lista encadeada contendo os elementos da posição 1 até 3.
'''

# Classe que implementa a Lista Encadeada
class Lista:
    
    # Classe interna que representa um nó da lista encadeada
    class No:
        
        # Inicializa o nó com um valor e uma referência ao próximo nó (pode ser None)
        def __init__(self, valor, proximo=None):
            self.valor = valor # Atribui o valor ao nó
            self.proximo = proximo # Atribui a referência ao próximo nó

        # Retorna a representação em string do valor do nó
        def __str__(self):
            return str(self.valor) # Converte o valor do nó em string

    # Inicializa a lista com cabeça, cauda e quantidade vazias
    def __init__(self, interavel=None):
        self.__cabeça = None # Define a cabeça da lista como None (vazia)
        self.__cauda = None # Define a cauda da lista como None (vazia)
        self.__quantidade = 0 # Inicializa a quantidade de nós na lista como 0

        # Se um objeto iterável for passado, insere seus elementos no final da lista
        if interavel is not None and hasattr(interavel, '__iter__'):
            for item in interavel: # Itera sobre os itens do iterável
                self.inserir_no_fim(item) # Insere cada item no final da lista
        elif interavel is not None:
            raise TypeError(f'O objeto {type(interavel)} nao e interavel') # Levanta um erro se o objeto não for iterável

    # Retorna a quantidade de elementos na lista
    def __len__(self):
        return self.__quantidade # Retorna o valor de quantidade

    # Retorna a representação em string da lista encadeada
    def __str__(self):
        return '['+', '.join([str(valor) for valor in self]) + ']' # Concatena os valores dos nós em uma string

    # Itera pelos nós da lista, permitindo uso em loops e compreensão de listas
    def __iter__(self): 
        atual = self.__cabeça # Começa a iteração na cabeça da lista
        while atual is not None: # Continua enquanto houver nós na lista
            yield atual.valor # Retorna o valor do nó atual
            atual = atual.proximo # Move para o próximo nó

    # Permite definir o valor em uma posição específica usando a sintaxe lista[posiçao] = valor
    def __setitem__(self, posiçao, valor):
        if posiçao < 0:
            posiçao = len(self) + posiçao # Ajusta a posição para suportar índices negativos

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida') # Levanta erro se a posição for inválida
        
        atual = self.__cabeça # Começa na cabeça da lista
        for i in range(posiçao): # Itera até a posição desejada
            atual = atual.proximo # Avança para o próximo nó

        atual.valor = valor # Define o novo valor no nó desejado

    # Permite deletar um nó da lista em uma posição específica usando a sintaxe del lista[posiçao]
    def __delitem__(self, posiçao):
        if posiçao < 0:
            posiçao = len(self) + posiçao # Ajusta a posição para suportar índices negativos
        
        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida.') # Levanta erro se a posição for inválida
        
        self.__quantidade -= 1 # Reduz a quantidade de nós na lista

        if posiçao == 0: # Se a posição for a cabeça da lista
            self.__cabeça = self.__cabeça.proximo # Define a nova cabeça como o próximo nó
            if self.__cabeça is None:
                self.__cauda = None # Se a lista ficar vazia, define a cauda como None
            return

        i = 0
        atual = self.__cabeça
        while atual.proximo is not None and i < posiçao - 1: # Itera até o nó anterior ao nó desejado
            atual = atual.proximo # Avança para o próximo nó
            i += 1
        
        if atual.proximo == self.__cauda: # Se o nó a ser removido for a cauda
            self.__cauda = atual # Define a nova cauda como o nó anterior

        atual.proximo = atual.proximo.proximo # Remove o nó desejado da lista

    # Permite acessar um valor por índice, ou uma fatia (slice) da lista
    def __getitem__(self, posiçao):
        if isinstance(posiçao, slice): # Se a posição for uma fatia
            passo = posiçao.step if posiçao.step is not None else 1 # Define o passo padrão como 1

            if passo == 0:
                raise ValueError('Passo nao pode ser igual a zero.') # Levanta erro se o passo for zero

            if passo > 0 :
                inicio = posiçao.start if posiçao.start is not None else 0 # Define o início padrão como 0
                fim = posiçao.stop if posiçao.stop is not None else len(self) # Define o fim padrão como o tamanho da lista

            else:
                inicio = posiçao.start if posiçao.start is not None else len(self) - 1 # Define o início padrão como o último índice
                fim = posiçao.stop if posiçao.stop is not None else -1 # Define o fim padrão como -1

            if inicio < 0:
                inicio = len(self) + inicio # Ajusta o início para suportar índices negativos

            if fim < 0 and posiçao.stop is not None:
                fim = len(self) + fim # Ajusta o fim para suportar índices negativos
            
            fatia = Lista() # Cria uma nova lista para a fatia
            if passo > 0:
                i = 0
                indices = range(inicio, fim, passo) # Cria uma faixa de índices para a fatia
                it = iter(self) # Cria um iterador para a lista
                while i < fim: # Itera até o fim da fatia
                    v = next(it) # Obtém o próximo valor
                    if i in indices: # Se o índice estiver na faixa
                        fatia.inserir_no_fim(v) # Insere o valor na fatia
                    i += 1
            else:
                for i in range(inicio, fim, passo): # Itera para fatias com passo negativo
                    fatia.inserir_no_fim(self[i]) # Insere o valor na fatia

            return fatia # Retorna a nova lista como fatia
                
        if posiçao < 0:
            posiçao = len(self) + posiçao # Ajusta a posição para suportar índices negativos
        
        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida.') # Levanta erro se a posição for inválida
        
        atual = self.__cabeça # Começa na cabeça da lista
        for i in range(posiçao): # Itera até a posição desejada
            atual = atual.proximo # Avança para o próximo nó
        
        return atual.valor # Retorna o valor do nó desejado

    # Insere um novo nó no final da lista
    def inserir_no_fim(self, valor):
        novo_no = self.No(valor) # Cria um novo nó com o valor fornecido
        self.__quantidade += 1 # Incrementa a quantidade de nós na lista

        if self.__cabeça is None: # Se a lista estiver vazia
            self.__cabeça = novo_no # Define a cabeça como o novo nó
            self.__cauda = novo_no # Define a cauda como o novo nó
        else:
            self.__cauda.proximo = novo_no # Define o próximo da cauda como o novo nó
            self.__cauda = novo_no # Atualiza a cauda para o novo nó

    # Insere um nó em uma posição específica na lista
    def inserir(self, posiçao, valor):
        if posiçao < 0:
            posiçao = len(self) + posiçao # Ajusta a posição para suportar índices negativos

        if posiçao < 0 or posiçao > self.__quantidade:
            raise IndexError('Posiçao invalida') # Levanta erro se a posição for inválida
        
        self.__quantidade += 1 # Incrementa a quantidade de nós na lista
        novo_no = self.No(valor) # Cria um novo nó com o valor fornecido

        if posiçao == 0: # Se a posição for no início da lista
            novo_no.proximo = self.__cabeça # Define o próximo do novo nó como a cabeça atual
            self.__cabeça = novo_no # Define a cabeça como o novo nó
            if self.__cauda is None:
                self.__cauda = novo_no # Se a lista estava vazia, define a cauda como o novo nó
            return
        
        i = 0
        atual = self.__cabeça
        while i < posiçao - 1: # Itera até o nó anterior ao desejado
            atual = atual.proximo # Avança para o próximo nó
            i += 1

        novo_no.proximo = atual.proximo # Define o próximo do novo nó como o próximo do nó atual
        atual.proximo = novo_no # Define o próximo do nó atual como o novo nó
        if novo_no.proximo is None:
            self.__cauda = novo_no # Se o novo nó for inserido no final, atualiza a cauda

    # Remove o primeiro nó que contém o valor fornecido
    def remover(self, valor):
        if self.__cabeça is None:
            raise ValueError('Lista Vazia.') # Levanta erro se a lista estiver vazia

        if self.__cabeça.valor == valor: # Se o valor estiver na cabeça
            self.__cabeça = self.__cabeça.proximo # Define a nova cabeça como o próximo nó
            self.__quantidade -= 1 # Reduz a quantidade de nós na lista
            if self.__cabeça is None:
                self.__cauda = None # Se a lista ficar vazia, define a cauda como None
            return

        anterior = self.__cabeça
        atual = self.__cabeça.proximo
        while atual is not None and atual.valor != valor: # Itera até encontrar o nó com o valor desejado
            anterior = atual # Avança o nó anterior
            atual = atual.proximo # Avança o nó atual

        if atual is None:
            raise ValueError(f'{valor} não encontrado.') # Levanta erro se o valor não for encontrado

        anterior.proximo = atual.proximo # Remove o nó com o valor desejado
        self.__quantidade -= 1 # Reduz a quantidade de nós na lista
        if anterior.proximo is None:
            self.__cauda = anterior # Se o nó removido era a cauda, atualiza a cauda

    # Retorna o índice da primeira ocorrência do valor fornecido
    def indice(self, valor):
        atual = self.__cabeça # Começa na cabeça da lista
        i = 0
        while atual is not None: # Itera pelos nós da lista
            if atual.valor == valor:
                return i # Retorna o índice se o valor for encontrado
            atual = atual.proximo # Avança para o próximo nó
            i += 1

        raise ValueError(f'{valor} não está na lista.') # Levanta erro se o valor não for encontrado

    # Conta quantas vezes o valor fornecido aparece na lista
    def contar(self, valor):
        atual = self.__cabeça # Começa na cabeça da lista
        count = 0
        while atual is not None: # Itera pelos nós da lista
            if atual.valor == valor:
                count += 1 # Incrementa o contador se o valor for encontrado
            atual = atual.proximo # Avança para o próximo nó
        return count # Retorna o total de ocorrências do valor

    # Remove e retorna o último nó da lista
    def pop(self):
        if self.__cabeça is None:
            raise ValueError('Lista Vazia.') # Levanta erro se a lista estiver vazia

        if self.__cabeça.proximo is None: # Se houver apenas um nó na lista
            valor = self.__cabeça.valor # Armazena o valor da cabeça
            self.__cabeça = None # Define a cabeça como None
            self.__cauda = None # Define a cauda como None
            self.__quantidade -= 1 # Reduz a quantidade de nós na lista
            return valor # Retorna o valor removido

        anterior = self.__cabeça
        atual = self.__cabeça.proximo
        while atual.proximo is not None: # Itera até o penúltimo nó
            anterior = atual # Avança o nó anterior
            atual = atual.proximo # Avança o nó atual

        valor = atual.valor # Armazena o valor do nó a ser removido
        anterior.proximo = None # Remove o último nó da lista
        self.__cauda = anterior # Atualiza a cauda para o penúltimo nó
        self.__quantidade -= 1 # Reduz a quantidade de nós na lista
        return valor # Retorna o valor removido

    # Reverte a ordem dos nós na lista
    def reverter(self):
        anterior = None
        atual = self.__cabeça
        self.__cauda = atual # Define a cauda como a cabeça original
        while atual is not None: # Itera pelos nós da lista
            proximo = atual.proximo # Armazena o próximo nó
            atual.proximo = anterior # Inverte a referência do próximo nó
            anterior = atual # Avança o nó anterior
            atual = proximo # Avança o nó atual
        self.__cabeça = anterior # Define a cabeça como o último nó original

    # Retorna uma cópia da lista encadeada
    def copiar(self):
        copia = Lista() # Cria uma nova lista vazia
        atual = self.__cabeça
        while atual is not None: # Itera pelos nós da lista original
            copia.inserir_no_fim(atual.valor) # Insere cada valor na cópia
            atual = atual.proximo # Avança para o próximo nó
        return copia # Retorna a nova lista como cópia

    # Limpa a lista, removendo todos os nós
    def limpar(self):
        self.__cabeça = None # Define a cabeça como None
        self.__cauda = None # Define a cauda como None
        self.__quantidade = 0 # Reseta a quantidade de nós na lista

    # Conta quantas vezes o valor fornecido aparece na lista
    def contar(self, valor):
        contador = 0 # Inicializa o contador para rastrear ocorrências do valor

        for elemento in self: # Itera por todos os elementos da lista
            if elemento == valor: # Verifica se o elemento atual é igual ao valor procurado
                contador += 1 # Incrementa o contador se o valor for encontrado

        return contador # Retorna o total de ocorrências do valor


    # Retorna um iterador que percorre a lista de trás para frente
    def __reversed__(self):
        return self[::-1] # Retorna a lista inversa usando slicing


    # Reverte a ordem dos elementos na lista
    def reverter(self):
        revertido = reversed(self) # Cria um iterador que percorre a lista na ordem inversa
        self.limpar() # Limpa a lista original
        self.estender(revertido) # Adiciona os elementos do iterador invertido à lista original


    # Retorna uma cópia da lista
    def copiar(self):
        return self[:] # Retorna uma nova lista que é uma cópia da original, usando slicing
