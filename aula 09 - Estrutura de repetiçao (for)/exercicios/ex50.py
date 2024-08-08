# crie um algoritimo que recebe 6 numeros inteiros e soma apenas os pares
count = 0
s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0 :
      s += n
      count += 1
print("FIM")
print(s)
print('Voce adicionou {} numeros pares'.format(count))