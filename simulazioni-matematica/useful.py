import numpy as np 
import math

def counter(obj,matrix):
    ''' this function return the number of elements (obj) in a matrix (matrix) '''
    count = 0
    shape = matrix.shape
    for y in range(shape[0]):
        for x in range(shape[1]):
            if matrix[y,x] == obj:
                count += 1
    return count

def condo_trig(tag=0):
    '''prints when triggered'''
    print('condition was triggered, tag=',tag)


def filling_randint(dens):
    ''' given the density it return a list touple containing the extremes to give to randint '''
    cifre = math.floor(100/dens)
    elements = []
    for i in range(cifre):
        elements.append(i)
    tup = (elements[0],elements[-1])
    return tup[1]

def somma(lista):
    ''' data una lista restituisce la somma dei suoi valori'''
    somma  = 0
    for x in range(len(lista)):
        somma += lista[x]

    return somma

