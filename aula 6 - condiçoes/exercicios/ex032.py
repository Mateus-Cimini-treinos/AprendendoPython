#crie um algoritimo que le um ano e identifica se ele e bissexto

year = 2024

''' int(input('Qual ano vc quer conferiri? '))'''

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print('O ano e bissexto')
        else : 
             print('O ano nao e bissexto')
    else : 
         print('O ano nao e bissexto')
else : 
    print('O ano nao e bissexto')
