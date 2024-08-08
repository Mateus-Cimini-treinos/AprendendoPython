# crie um programa que mostre a tabuada do numero solicitado ate que eu digite um numero negativo
print("Tabuada de 0 a 10")
while True:
    number = int(input('Digite um numero para ve a tabuada dele  '))
    if number < 0 :
        break
    print(f'tabuada de {number}\n')
    for multiplicador in range(11):
        r = number * multiplicador
        print(f'{number} X {multiplicador} = {r}')
print('fim')
