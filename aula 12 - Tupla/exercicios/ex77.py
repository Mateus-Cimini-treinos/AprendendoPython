#crie um algoritimo que tenha uma tupla com varias palavras depois vc deve mostrar para cada palavra quais sao as suas vogais

# Lista de personagens
personagens_lol = (
    "Ahri",
    "Yasuo",
    "Lux",
    "Jinx",
    "Garen",
    "Zed",
    "Ashe"
)

# Variáveis para armazenar as vogais encontradas em cada personagem
for personagem in personagens_lol:
    sima = 'a' if 'a' in personagem.lower() else ''
    sime = 'e' if 'e' in personagem.lower() else ''
    simi = 'i' if 'i' in personagem.lower() else ''
    simo = 'o' if 'o' in personagem.lower() else ''
    simu = 'u' if 'u' in personagem.lower() else ''

    print(f'{personagem} tem as vogais {sima} {sime} {simi} {simo} {simu}')
