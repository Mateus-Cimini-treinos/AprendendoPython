#crie um programa que recebe o nome de uma cidade e ela retorna dizendo se sua cidade tem "Sao" no nome

City = str(input('Qual o nome da sua cidade >> '))

check = 'São' in City

if(check == True): print('A sua cidade tem "São" no nome')
else :  print('Sua cidade nao tem "São" no nome')