#crie um programa que o usuario deve cadastrar 5 numeros e o programa deve ja cadastralos na posiçao correta sem usar sort

lista = []
for c in range(0,5):
    n = int(input('digite um valor '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('valor foi adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista')
                break
            pos += 1
print(f'os valores adicionados sao {lista}')