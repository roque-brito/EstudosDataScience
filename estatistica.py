from collections import Counter
from typing import List
import matplotlib.pyplot as plt

num_amigos = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

contagem_amigos = Counter(num_amigos)

xs = range(101)                             # range até 100 (n-1)
ys = [contagem_amigos[x] for x in xs]       # a altura indica o nº de amigos

# Gerando um histograma do número de pessoas por número de amigos:
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histograma de Contagem de amigos')
plt.xlabel('Nº de pessoas')
plt.ylabel('Nº de amigos')
#plt.show()

# Número de pontos de dados:
num_pontos = len(num_amigos)
print(f'Número total de pontos: {num_pontos}')

# Valores mais alto e mais baixo da lista:
maior_valor = max(num_amigos)
menor_valor = min(num_amigos)
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')

## Casos especiais para verificar posições específicas:
#classifica_valores = sorted(num_amigos)                 # alinha a lista do menor valor -> maior valor: [1, ..., 100]
#menor_valor_ordenado = classifica_valores[0]
#print(f'Menor valor ordenado: {menor_valor_ordenado}')
#segundo_menor_valor = classifica_valores[1]
#print(f'Segundo menor valor na lista ordenada: {segundo_menor_valor}')
#maior_valor_ordenado = classifica_valores[-1]
#print(f'Maior valor na lista ordenada: {maior_valor_ordenado}')
#segundo_maior_valor = classifica_valores[-2]
#print(f'Segundo maior valor na lista ordenada: {segundo_maior_valor}')

# TENDÊNCIAS CENTRAIS:

# MÉDIA:
def media(xs: List[float]) -> float:
    '''Cálculo da média simples de valores da lista: List[float] -> float'''
    return sum(xs) / len(xs)

print(f'Média da lista número de amigos: {media(num_amigos)}') # MEDIA = 7,333

# MEDIANA:
vetor = [1, 6, 2, 3, 5] # O tamanho da lista é 5 (ímpar). A madiana será o valor do meio da lista ordenada
vetor = sorted(vetor)
mediana_vetor = vetor[5 // 2]                         # posição do meio se o tamanho da lista for ímpar
print(f'A mediana da lista "vetor" é: {mediana_vetor}')

# As funções sublinhadas indicam que são funções "privadas", pois devem ser chamdas pela função da mediana
# e não por outros usuários da biblioteca de estatísticas.
def _mediana_impar(xs: List[float]) -> float:
    '''Se len(xs) for ímpar, a mediana será o elemento do meio'''
    return sorted(xs)[len(xs) // 2]

def _mediana_par(xs: List[float]) -> float:
    '''Se len(xs) for par, a mediana será a média dos dois elementos do meio'''
    sorted_xs = sorted(xs)
    hi_ponto_medio = len(xs) // 2       # p.e.: comprimento 5 => hi_ponto_medio == 2
    return (sorted_xs[hi_ponto_medio - 1] + sorted_xs[hi_ponto_medio]) / 2

def mediana(v: List[float]) -> float:
    '''Encontra o valor do meio em v'''
    return _mediana_par(v) if len(v) % 2 == 0 else _mediana_impar(v)

assert mediana([1, 10, 2, 9, 5]) == 5
assert mediana([1, 9, 2, 10]) == (9 + 2) / 2
assert mediana([1, 6, 2, 3, 5]) == 3


print(mediana(num_amigos))





