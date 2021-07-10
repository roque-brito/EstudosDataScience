# TENDÊNCIAS CENTRAIS: MEDIANA
from collections import Counter
from typing import List

num_amigos = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
xs = range(101)                             # range até 100 (n-1)

vetor = [1, 6, 2, 3, 5] # O tamanho da lista é 5 (ímpar). A madiana será o valor do meio da lista ordenada
vetor = sorted(vetor)
mediana_vetor = vetor[5 // 2]                          # posição do meio se o tamanho da lista for ímpar
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