"Aula de loop mais expecificamente loop for"


# Loop que imprime "hello, world!" 5 vezes
for hello in range(0, 5): 
    print('hello, world!')
print("FIM!!")

# Loop que imprime números de 0 a 5
for n in range(0, 6):
    print(n)
print('FIM')

# Loop que imprime números de 0 a 5, pulando de 2 em 2
for n in range(0, 6, 2):
    print(n)
print('FIM')

# Loop que imprime números de 0 até o número digitado pelo usuário
numbers = int(input('Digite um numero: '))
for num in range(0, numbers + 1):
    print(num)
print('FIM')

# Loop que imprime números a partir de um número inicial até um final, com um passo definido pelo usuário
start = int(input('O numero inicial: '))
end = int(input('O numero final: '))
step = int(input('passos: ')) 
for num in range(start, end, step):
    print(num)
print('FIM')

# Loop que solicita ao usuário 3 valores e calcula a soma total
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print("FIM")
print(s)
