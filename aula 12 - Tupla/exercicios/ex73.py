# faça um algoritimo que com uma tupla com os times do brasileirao mostre
# apenas os 5 primeiros colocados
# os ultimos 4 colocados
# uma lista em ordem alfabetica
# em que posiçao esta o flamengo

times_brasileirao_2023 = (
    "Botafogo", "Palmeiras", "Atlético-MG", "Grêmio", "Flamengo", 
    "Athletico-PR", "Fluminense", "Fortaleza", "São Paulo", 
    "Internacional", "Cruzeiro", "Bragantino", "Cuiabá", 
    "Corinthians", "Bahia", "Santos", "Goiás", "Vasco da Gama", 
    "América-MG", "Coritiba"
)
print('Todos os times na ordem da classificaçao')
print(times_brasileirao_2023)
print('5 primeiros colocados')
print(times_brasileirao_2023[0:5])
print('os ultimos 4 colocados')
print(times_brasileirao_2023[-4:])
print('em ordem alfabetica')
print(sorted(times_brasileirao_2023))
pos = times_brasileirao_2023.index('Flamengo')
pos += 1
print(f'O flamengo esta na posiçao {pos}')