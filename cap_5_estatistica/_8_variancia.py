# VARIÂNCIA: uma medida mais complexa da DISPERSÃO. 
from collections import Counter
from typing import List
import math
#from scratch.linear_algebra import sum_of_squares
num_amigos = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
xs = range(101)           

def media(xs: List[float]) -> float:
    '''Calcula a média simples'''
    return sum(xs) / len(xs)

def sub_media(xs: List[float]) -> float:
    '''Traduza xs subtraindo sua média - para que o resultado tenha media 0'''
    x_bar = media(xs)
    return [x - x_bar for x in xs]

def soma_quadrados(xs: List[float]) -> float:
    # implementar ou encontrar bilbioteca ...

def variancia(xs: List[float]) -> float:
    '''Calcula a variância - quase o desvio quadrado médio da média'''
    assert len(xs) >= 2, "A variancia requer ao menso dois elementos"

    n = len(xs)
    desvio = sub_media(xs)
    return 

#if __name__ == '__main__':