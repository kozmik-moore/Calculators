# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:30:15 2018

@author: Kozmik
"""
from math import gcd
from matplotlib import pyplot as plt
import numpy as np

STOP = 50
MIN = -100
MAX = 100
INTERVAL = 5


def add_operators(l1, l2):
    tmp = []
    for i in range(len(l1)):
        tmp.append(l1[i] + l2[i])
    return tmp


def reduce(l):     # list of three integers
    tmp = l.copy()
    tmp.sort()
    a = gcd(int(tmp[0]), int(tmp[1]))
    b = gcd(a, int(tmp[2]))
    tmp = l.copy()
    for i in range(len(tmp)):
        tmp[i] = tmp[i]//b
    return tmp


def get_operators():
    system = []
    file = 'Input.txt'
    f = open(file, 'r')
    for line in f:
        tmp = line.rstrip().split(' ')
        for index in range(len(tmp)):
            tmp[index] = int(tmp[index])
        system.append(tmp)
    return system


def write(l):       # list of lists
    file = 'Output.txt'
    f = open(file, 'w')
    for item in l:
        if type(item[0]) is int: 
            f.write(str(item) + '\n')
        else:
            f.write(str(item[0]) + '  ' + str(item[1]) + '\n')
    f.close()


def get_vector(l):       # list
    if type(l[0]) is int:
        return l
    else:
        return l[0]


def plot(l):
    for item in l:
        v = get_vector(item)
        x = np.linspace(MIN, MAX, INTERVAL)
        y = (-1*v[0]/v[1])*x + (v[2]/v[1])
        plt.plot(x,y)
        
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.axis('scaled')
#    plt.show()
#    plt.figure(figsize=(5,5))
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    fig.savefig('test.png', dpi=100)


def explicit_eqs():
    main = get_operators()
    current = None
    start = len(main) - 1
    stop = STOP
    
    while start < len(main) and start < stop:
        current = get_vector(main[start])
        for index in range(start):
            if len(main) == stop:
                break
            new = add_operators(current, get_vector(main[index]))
            reduced = reduce(new)
            if reduced not in main:
                main.append(reduced)
            else:
                main.append([new, reduced])                
        start += 1
        
    write(main)
    plot(main)


def partition_eqs():
    main = get_operators()
    current = None
    start = len(main) - 1
    stop = STOP
    
    while start < len(main) and start < stop:
        current = get_vector(main[start])
        for index in range(start):
            if len(main) == stop:
                break
            new = add_operators(current, get_vector(main[index]))
            if new not in main:
                main.append(new)
        start += 1
    write(main)
    plot(main)


partition_eqs()
