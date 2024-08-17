# Peça ao usuário para inserir três notas. Converta as entradas para float, calcule a média e exiba o resultado.

nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
nota3 = float(input('Digite a terceira nota '))

somanota = nota1 + nota2 + nota3
    
media = somanota / 3

print(f'A media das suas notas sao {media:.2f}')