# aula de while mais especificamente breck que e usado para parar um loop while

n = 0
while True:
    cont = int(input('Digite um número (ou 0 para sair): '))
    if cont == 0:
        break
    n += 1
    print(f'Número de iterações: {n}')
print('Fim')
