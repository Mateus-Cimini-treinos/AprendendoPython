# aula sobre Linked lists
from typing import Any


class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo


        def __str__(self):
            return str(self.valor)



    def __init__(self, interavel=None):
        self.__cabeça = None
        self.__cauda = None
        self.__quantidade = 0

        if interavel is not None and hasattr(interavel, '__iter__'):
            for item in interavel:
                self.inserir_no_fim(item)
        elif interavel is not None:
            raise TypeError(f'O objeto {type(interavel)} nao e interavel')


    def __len__(self):
        return self.__quantidade
    

    def __str__(self):
        return '['+', '.join([str(valor) for valor in self]) + ']'
    

    def __iter__(self): 
        atual = self.__cabeça
        while atual is not None:
            yield atual.valor
            atual = atual.proximo


    def __setitem__(self, posiçao, valor):
        if posiçao < 0 :
            posiçao = len(self) + posiçao

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')
        
        atual = self.__cabeça
        for i in range(posiçao):
            atual = atual.proximo

        atual.valor = valor


    def __delitem__(self, posiçao):
        if posiçao < 0:
            posiçao = len(self) + posiçao
        
        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida.')
        
        self.__quantidade -= 1

        # removendo da cabeça
        if posiçao == 0:
            self.__cabeça = self.__cabeça.proximo
            if self.__cabeça is None:
                self.__cauda = None
            return

        i = 0
        atual = self.__cabeça
        # buscando elemento anterior a posiçao que a gente quer remover
        while atual.proximo is not None and i <posiçao - 1:
            atual = atual.proximo
            i += 1
        
        # removendo a cauda
        if atual.proximo == self.__cauda:
            self.__cauda = atual


        # estamos removendo o elemento desejado
        atual.proximo = atual.proximo.proximo



    def __getitem__(self, posiçao):
        if isinstance(posiçao, slice):
            passo = posiçao.step if posiçao.step is not None else 1

            if passo == 0:
                raise ValueError('Passo nao pode ser igual a zero.')

            if passo > 0 :
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
            # se o passo for positivo, vamos usar o lazy evaluation com __iter__
            if passo > 0:
                i = 0
                indices = range(inicio, fim, passo)
                it = iter(self)
                while i < fim:
                    v = next(it)
                    if i in indices:
                        fatia.inserir_no_fim(v)
                    i += 1
            else: # se for negativo, vamos usar __getitem__
                for i in range(inicio, fim, passo):
                    fatia.inserir_no_fim(self[i])

            return fatia
                

        if posiçao < 0:
            posiçao = len(self) + posiçao

        if posiçao < 0 or posiçao >= self.__quantidade:
            raise IndexError('Posiçao invalida')
        
        # buscando o elemento que esta na posiçao desejada
        atual = self.__cabeça
        for i in range(posiçao):
            atual = atual.proximo

        return atual.valor
    

    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        # quando a lista é vazia
        if self.__cabeça is None:
            self.__cabeça = novo
            self.__cauda = novo
            return
        
        self.__cauda.proximo = novo
        self.__cauda = novo

    def inserir(self, posiçao, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        
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

        if atual.proximo is None: # inserir na cauda (ultima posiçao)
            self.__cauda = novo

        novo.proximo = atual.proximo
        atual.proximo = novo 

    
   






lista = Lista(range(50))

print(lista)
del(lista[10])
print(lista)
del(lista[0])
print(lista)
del(lista[1])
print(lista)
del(lista[-1])
print(lista)
lista[-1] = 'Mateus'
print(lista)