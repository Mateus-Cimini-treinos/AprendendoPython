#faça um programa que recebe 9 valores e guarda em uma unica lista e depois mostra esses valores em uma matriz 3X3

matriz = []
for c in range(0,9) :
    matriz.append(int(input('digite um valor ')))

print(f'''
({matriz[0]:^5}) ({matriz[1]:^5}) ({matriz[2]:^5})
({matriz[3]:^5}) ({matriz[4]:^5}) ({matriz[5]:^5})
({matriz[6]:^5}) ({matriz[7]:^5}) ({matriz[8]:^5})
''')
print(matriz)