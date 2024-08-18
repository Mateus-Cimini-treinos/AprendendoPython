# aula sobre Linked lists
class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo


        def __str__(self):
            return str(self.valor)



    def __init__(self):
        self.__cabeça = None
        self.__quantidade = 0


    def __len__(self):
        return self.__quantidade
    

    def __str__(self):
        return '['+', '.join([str(valor) for valor in self]) + ']'
    

    def __iter__(self): 
        atual = self.__cabeça
        while atual is not None:
            yield atual.valor
            atual = atual.proximo


    def __getitem__(self, posiçao):
        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')
        
        # buscando o elemento que esta na posiçao desejada
        atual = self.__cabeça
        for i in range(posiçao):
            atual = atual.proximo

        return atual.valor

    def inserir(self, posiçao, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # quando a lista estiver vazia
        if self.__cabeça is None:
            self.__cabeça = novo
            return
        
        # inserir na cabeça (primeira posiçao)
        if posiçao <= 0:
            novo.proximo = self.__cabeça
            self.__cabeça = novo
            return
        
        i = 0 # indice do elemento atual
        atual = self.__cabeça
        # buscando o elemento anterior a posiçao que a gente quer inserir
        while atual.proximo is not None and i < posiçao -1:
            atual = atual.proximo
            i += 1

        novo.proximo = atual.proximo
        atual.proximo = novo 

    
   






lista = Lista()

print(lista)
lista.inserir(0, 5)
lista.inserir(1, 20)
lista.inserir(2, 15)
lista.inserir(2, 7)
print(lista)