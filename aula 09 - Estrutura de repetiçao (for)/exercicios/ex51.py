# Entrada de dados
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicialização das variáveis
termo_atual = primeiro_termo

print("Os 10 primeiros termos da PA são:")

# Laço para calcular e imprimir os 10 primeiros termos
for i in range(10):
    print(termo_atual)
    termo_atual += razao  # Atualiza o termo atual para o próximo termo da PA

print('Fim')
