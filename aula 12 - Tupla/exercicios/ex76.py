# crie um algoritimo que tenha uma tupla unica com nomes de produtos e seus respectivos preços
#no final mostre uma listagem de preços organizando os dados em forma tabular

produtosePreços = (
    ("pão"), 
    (0.60),
    ("feijão"), 
    (3.50),
    ("leite"),
    (2.00),
    ("arroz"),
    (5.00),
    ("macarrão"),
    (1.75),
    ("açúcar"), 
    (2.30),
    ("óleo"), 
    (4.25),
    ("café"), 
    (7.90)
)

print('-' * 30)
print (' '* 10 , 'Mercado', ' ' * 20)
print('-' * 30)
print(f'''
{produtosePreços[0]}...................R$ {produtosePreços[1] :.2f}
{produtosePreços[2]}................R$ {produtosePreços[3]:.2f}
{produtosePreços[4]}.................R$ {produtosePreços[5]:.2f}
{produtosePreços[6]}.................R$ {produtosePreços[7]:.2f}
{produtosePreços[8]}..............R$ {produtosePreços[9]:.2f}
{produtosePreços[10]}................R$ {produtosePreços[11]:.2f}
{produtosePreços[12]}..................R$ {produtosePreços[13]:.2f}
{produtosePreços[14]}..................R$ {produtosePreços[15]:.2f}
''')

print('-' * 30)