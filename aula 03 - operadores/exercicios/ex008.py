'''crie um algoritimo que recebe um valor em metros e devolve em centimetros e milimetros'''

number = float(input('Digite um valor em metros'))

cm = number * 100

mm = cm * 10

print('Você digitou {:.0f}M \nEm centimetros {:.0f}Cm \nEm milimetros {:.0f}Mm'.format(number, cm, mm))