# TENDÊNCIAS CENTRAIS: QUANTIL
# uma generalização da MEDIANA
from collections import Counter
from typing import List

num_amigos = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
xs = range(101)           # Lembre: n = 101 -> range até 100, ou seja, (n-1)

def quantil(xs: List[float], p: float) -> float:
    '''Retorna o elemento do p-iésimo-percentil em xs'''
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]
    
assert quantil(num_amigos, 0.10) == 1
assert quantil(num_amigos, 0.25) == 3
assert quantil(num_amigos, 0.75) == 9
assert quantil(num_amigos, 0.90) == 13
