#crie um programa que aprova o finaciamento de uma casa, o programa vai receber o valor da casa e o salario do comprandor e em quantos anos ele vai pagar, calcule o valor da prestaçao mensal sabendo que o valor da pacela nao pode ser maior a 30% do salario

#inputs sobre valores
housePrice = int(input('Qual o valor da casa? '))
wage = float(input('Qual e a quantia do seu salario mensal? '))
years = int(input('Em quantos anos voce vai pagar? '))

#tranformando anos em meses
months = years * 12

#dividindo valor da casa pelo meses para saber valor da parcela
installmentValue = housePrice / months

#descobrindo qual e o valor de 30* do salario
passingScore = wage - (wage * 70 / 100)

print('Analisando sua proposta')

#se o 30% do salario for menor que a pacela o imprestimo e recusado
if installmentValue > passingScore :
    print('O financiamneto nao foi aprovado porque o valor da parcela e maior que 30% do seu salario mensal')
#se o 30% do salario for maior que o valor da pacela e aprovado e o print mostra os valores
else : 
    print('O finaciamento foi aprovado vc vai pagar em {} meses e o valor da parcela vai ser de {:.2f} e 30% do seu salario equivale a {}'.format(months,installmentValue,passingScore))

