from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('ano de nacimento'))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('ao todo tivemos {} pessoas menores de idade'.format(totmenor))