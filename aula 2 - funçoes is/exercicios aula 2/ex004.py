'''crie um sistema que o input recebe uma resposta e o sistema retorna informaçoes sobre o input'''

txt = input('Digite algo:')

print('O tipo primitico do objeto e:', type(txt))
print('So tem espaços? ' , txt.isspace())
print('So tem letras?' , txt.isalpha())
print('E decimal?' , txt.isdecimal())
print('Esta escrito somente em letra maisculas?' , txt.isupper())
print('E um numero?' , txt.isnumeric())
print('E alfanumerico?' , txt.isalnum())
print('Ele esta em minuscula?' , txt.islower())
print('Ela esta captalizada?' , txt.istitle())