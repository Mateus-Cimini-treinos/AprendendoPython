# aula sobre Linked lists
class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo


    def __init__(self):
        self.__cabeça = None
        self.__quantidade = 0


    def __len__(self):
        return self.__quantidade
    

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

print(len(lista))
lista.inserir(0, 5)
lista.inserir(1, 20)
lista.inserir(2, 15)
lista.inserir(2, 7)
print(len(lista))

print(f'O elemento da posiçao 0 é {lista[0]}')
print(f'O elemento da posiçao 1 é {lista[1]}')
print(f'O elemento da posiçao 2 é {lista[2]}')
print(f'O elemento da posiçao 3 é {lista[3]}')


for e in lista:
    print(e)