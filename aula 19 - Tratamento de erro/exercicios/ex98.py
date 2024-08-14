def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mERRO: O usuario deixou campos em branco. entao o resultado sera: \033[m')
            return 0
        else:
            return n
        


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um numero real valido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31ERRO: o usuario deixou campos em branco. entao o valor sera: \033[m')
            return 0
        else:
            return n

num1 = leiaInt('Digite um numero inteiro ')
num2 = leiaFloat('Digite um numero real ')
print(f'O valor digitado para inteiro foi {num1} e para real foi {num2}') 