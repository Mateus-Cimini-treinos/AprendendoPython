#  Peça ao usuário para digitar uma temperatura em Celsius. Converta a entrada para um número com ponto flutuante e, em seguida, converta a temperatura para Fahrenheit usando a fórmula: F = (C * 9/5) + 32. Exiba o resultado.


celsius = input("Digite a temperatura em graus Celsius: ")

celsius = float(celsius)


fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit}")
