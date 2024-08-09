#  crie um algoritimo que  tem uma tupla prenchida de numero extenso de 0 a 20 seu programa deve mostrar o numero que vc digitar

numerosExtenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
    'doze', 'treze', 'quatorze', 'quinze', 
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    if num < 0 or num > 20:
        print('Você digitou um número inválido. Tente novamente.')
    else:
        print(f'Você pediu o número {numerosExtenso[num]}')
        break
