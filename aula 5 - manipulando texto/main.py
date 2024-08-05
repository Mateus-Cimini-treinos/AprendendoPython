# Aula sobre manipulação de texto em Python
# FATIAMENTO: Manipulação de uma string, como dividir, pegar letras específicas, etc.
# ANÁLISE: Análise de uma string, como determinar o comprimento ou contar ocorrências.
# TRANSFORMAÇÃO: Alterações em uma string, como mudar para maiúsculas ou substituir caracteres.
# DIVISÃO: Dividir uma string em partes, útil para manipulação posterior.

frase = 'Mateus é lindo'  # String usada para demonstração

print('''
      fysduigfyreidufgherdiuogfhjredogfhuidohgiufdhgufidhguifh
      dgiujhtfuighfuigjhfnugjihfngujiuhfnbdjighfdjihgfduijghnfiujd
      hngbfiujdhnbgjifdhgbniujfdhnbgiujfdhnbgiughusdghusdfhgyufdhgu
      ftsyedgfgytdusgfyuergfryeuihgrfihgdrfuiehguifohegrdhrugdhhgt
      ''') #fazendo print mostrar o texto ja formatado



print('-'*60 + '\nFATIAMENTO')
# FATIAMENTO: Extraindo partes específicas da string

letra = frase[5]  # Pega a letra na posição 5 (index começa em 0)
nome = frase[0:6]  # Pega os caracteres do início até a posição 6 (não inclusa)
fatiando_de_2_em_2 = frase[0:14:2]  # Pega caracteres do início ao fim, pulando de 2 em 2
nome2 = frase[:7]  # Pega os primeiros 7 caracteres
adjetivo2 = frase[9:]  # Pega todos os caracteres a partir da posição 9
fatiando_a_partir_do_5 = frase[5::2]  # Pega caracteres a partir da posição 5, pulando de 2 em 2

print('A frase inteira = {}\nA letra selecionada = {}\nO nome = {}\nFatiado de 2 em 2 = {}\nO nome denovo = {}\nO adjetivo denovo = {}\nTexto fatiado e começando na letra 6 = {}'.format(frase, letra, nome, fatiando_de_2_em_2, nome2, adjetivo2, fatiando_a_partir_do_5))

print('-'*60 + '\nANÁLISE')
# ANÁLISE: Funções para analisar a string

comprimento = len(frase)  # Obtém o comprimento da string
print(comprimento)

quantidade_e = frase.count("e")  # Conta quantas vezes 'e' aparece na string
print(quantidade_e)

quantidade_e_fatiada = frase.count('e', 0, 6)  # Conta 'e' do início até a posição 6
print(quantidade_e_fatiada)

posicao_us = frase.find('us')  # Encontra a posição de 'us' na string
print(posicao_us)

nao_existe = frase.find('feio')  # Tenta encontrar 'feio' (não existe)
print(nao_existe)

existe = 'lindo' in frase  # Verifica se 'lindo' está na string
print(existe)

print('-'*60 + '\nTRANSFORMAÇÃO')
# TRANSFORMAÇÃO: Modificações na string

trocando = frase.replace('lindo', 'gostoso')  # Substitui 'lindo' por 'gostoso'
print(trocando)

maiuscula = frase.upper()  # Transforma todos os caracteres em maiúsculas
print(maiuscula)

minuscula = frase.lower()  # Transforma todos os caracteres em minúsculas
print(minuscula)

nome_maiusculo = frase.lower()  # Transforma todos os caracteres em minúsculas (não necessário, já existe "minuscula")

capitalizando = frase.capitalize()  # Capitaliza a primeira letra e torna o resto minúsculo
print(capitalizando)

transformando_titulo = frase.title()  # Capitaliza a primeira letra de cada palavra
print(transformando_titulo)

frase2 = '  Mateus é foda   '  # String com espaços extras para demonstração

corrigindo_espacos = frase2.strip()  # Remove espaços extras do início e fim
print(corrigindo_espacos)

corrigindo_espacos_fim = frase2.rstrip()  # Remove espaços extras do final
print(corrigindo_espacos_fim)

corrigindo_espacos_comeco = frase.lstrip()  # Remove espaços extras do início
print(corrigindo_espacos_comeco)

print('-'*60 + '\nDIVISÃO')
# DIVISÃO: Dividindo a string em partes

lista_frase = frase.split()  # Divide a string em uma lista de palavras
print(lista_frase)

juntando = '_'.join(lista_frase)  # Junta a lista de palavras em uma string, separadas por '_'
print(juntando)
