from collections import Counter

num_amigos = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

contagem_amigos = Counter(num_amigos)

# Número de pontos de dados:
num_pontos = len(num_amigos)
print(f'Número total de pontos: {num_pontos}')

# Valores mais alto e mais baixo da lista:
maior_valor = max(num_amigos)
menor_valor = min(num_amigos)
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')

# Casos especiais para verificar posições específicas:
classifica_valores = sorted(num_amigos)                 # alinha a lista do menor valor -> maior valor: [1, ..., 100]
menor_valor_ordenado = classifica_valores[0]
print(f'Menor valor ordenado: {menor_valor_ordenado}')
segundo_menor_valor = classifica_valores[1]
print(f'Segundo menor valor na lista ordenada: {segundo_menor_valor}')
maior_valor_ordenado = classifica_valores[-1]
print(f'Maior valor na lista ordenada: {maior_valor_ordenado}')
segundo_maior_valor = classifica_valores[-2]
print(f'Segundo maior valor na lista ordenada: {segundo_maior_valor}')
