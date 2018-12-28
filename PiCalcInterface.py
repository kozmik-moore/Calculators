# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:58:08 2018

@author: Kozmik
"""

import PiCalc_v2

loop = True

while loop:
    print('\nEnter parameters with comma separators or press \'q\' to quit:')
    #num: number of samples
    #size: sample size
    #radius: length of circle radius
    #dims: 
    values = input()
#    num, size, radius, dims = None
    if values == 'q':
        break
    values = values.split(',')
    for i in range(len(values)):
        values[i] = int(values[i])
    calc = PiCalc_v2.PiCalculator(values[0], values[1], values[2])
#    calc = PiCalc.PiCalculator(num, size, radius, dims)

    calc.runAndPrint()
    
    loop = input('Continue? (y/n)\n')
    if loop == 'n':
        loop = False