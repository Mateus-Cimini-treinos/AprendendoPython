#crie um algoritimo que descobre se uma frase e um palimetro

frase = str(input("DIGITE UMA FRASE ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = 0
for letra in range(len(junto) -1 , -1, -1 ):
    inverso += junto[letra]
if junto == inverso :
    print('E um palidromo')
else:
    print('nao e um palimedro')