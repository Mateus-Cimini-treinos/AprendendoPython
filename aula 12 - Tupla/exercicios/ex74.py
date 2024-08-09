#crie um algoritimo que vai gerar 5 numeros para uma tupla e depopis vai mostrar os numeros gerados e qual o maior e qual o menor

import random
numerosTupla = (
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
)

menor = min(numerosTupla)
maior = max(numerosTupla)

print(numerosTupla)
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
