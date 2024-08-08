# crie um algoritimo que recebe um numero N e mostra na tela os n primeiros elementos de uma sequencia fibonacci

p = 0
s = 1
f = int(input('Quantos termos da sequencia de Fibonacci voce deseja ve?  '))
while f > 1 :
    print(s, end=' ')
    p, s = s, p + s
    f -= 1
    



