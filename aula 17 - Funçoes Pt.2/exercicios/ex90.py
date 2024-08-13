#crie um programa que rerece o ano de nacimento de uma pessoa e retorna se ela tem o voto obrigatorio ou nao

from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Nao vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opicional'
    else :
        return f'Com {idade} anos: Voto obrigatorio'
    
nasc = int(input('Em que ano vc nasceu? '))
print(voto(nasc))