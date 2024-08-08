#crie um programa que recebe 2 valores, e depois aparece um menu pedindo que escolhe uma opçao
'''
1 = somar >>
2 = multiplicar >>
3 = qual e maior >>
4 = digitar novos numeros
5 = sair do programa >>
'''

n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo valor '))
escolha = 6
while escolha != 5 :
    escolha = int(input('escolha uma opçao!\n ( 1 ) para somar\n ( 2 ) para multiplicar\n ( 3 ) para saber qual e maior\n ( 4 ) para trocar numeros\n ( 5 ) para finalizar programa\n  '))
    if escolha == 1 :
        r =  n1 + n2
        print('A resposta da soma entre {} + {} = {}'.format(n1,n2,r))
    if escolha == 2 :
        r = n1 * n2 
        print('A multiplicaçao de {} X {} = {}'.format(n1,n2,r))
    if escolha == 3 :
        if n1 > n2 :
            print('{} e maior que {}'.format(n1,n2))
        else :
            print('{} e maior que {}'.format(n2,n1))
    if escolha == 4 :
        n1 = int(input('Digite o primeiro valor '))
        n2 = int(input('Digite o segundo valor '))
    print('--' * 50)
print('Voce digitou 5 e o programa acabou')
