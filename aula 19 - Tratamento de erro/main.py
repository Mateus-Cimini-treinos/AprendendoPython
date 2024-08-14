# Aula de tratamento de erro em Python

# Primeiro bloco de código com tratamento genérico de exceções

try:
    # Tenta converter o valor de entrada para um inteiro
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    
    # Tenta realizar a divisão dos dois números
    c = a / b

# Captura qualquer exceção que possa ocorrer e armazena na variável 'erro'
except Exception as erro:
    # Exibe uma mensagem indicando que houve um erro e mostra a classe do erro ocorrido
    print(f'Infelizmente deu um erro :( O erro foi: {erro.__class__} ')

# Bloco que será executado se não houver exceções no try
else:
    # Exibe o resultado da divisão se tudo correr bem
    print(f'O resultado da divisão de {a} / {b} = {c}')

# Bloco que será executado independentemente de ocorrer uma exceção ou não
finally:
    # Exibe uma mensagem final de encerramento
    print('Volte sempre! Encerramos por hoje')





# Segundo bloco de código com tratamento específico de exceções

try:
    # Tenta converter o valor de entrada para um inteiro
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    
    # Tenta realizar a divisão dos dois números
    c = a / b

# Captura exceções específicas para problemas de tipo ou valor incorreto
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou')

# Captura a exceção de divisão por zero
except ZeroDivisionError:
    print('Você tentou dividir um valor por zero')

# Captura a exceção quando o usuário interrompe a entrada de dados
except KeyboardInterrupt:
    print('O usuário deixou um dos campos em branco')

# Captura qualquer outra exceção não prevista nas capturas anteriores
except Exception as erro:
    # Exibe uma mensagem com a causa específica do erro
    print(f'Infelizmente deu um erro :( O erro foi: {erro.__cause__} ')

# Bloco que será executado se não houver exceções no try
else:
    # Exibe o resultado da divisão se tudo correr bem
    print(f'O resultado da divisão de {a} / {b} = {c}')

# Bloco que será executado independentemente de ocorrer uma exceção ou não
finally:
    # Exibe uma mensagem final de encerramento
    print('Volte sempre! Encerramos por hoje')
