# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:45:38 2018

@author: Kozmik
"""

import numpy as np
import random

class SystemSolver:
    def __init__(self, filepath=None):
        """Data format is a text file organized into two columns, domain first
        and codomain second"""
        self.x_values = []
        self.y_values = []
        self.solution = []
        self.polynomial = ''
        self.domain = {'xmin':-5, 'xmax':5, 'ymin':-5, 'ymax':5, 'num':3, 
                       'int_only': True}
        
        self.extractData(file=filepath)
        
    def extractData(self, file=None):
        try:
            if file:
                f = open(file)
            else:
                f = open('Coord_data.txt')
            data = f.readlines()
            f.close()
            self.x_values.clear()
            self.y_values.clear()
            for r in data:
                pair = r.rstrip().split()
                self.x_values.append(float(pair[0]))
                self.y_values.append(float(pair[1]))
            x = self.x_values.copy()
            x.sort()
            xmin = x[0]
            xmax = x[-1]
            y = self.y_values.copy()
            y.sort()
            ymin = y[0]
            ymax = y[-1]
            int_only = True
#            for i in range(len(x)):
#                if type(x[i]) is not int or type(y[i]) is not int:
#                    int_only = False
#                    break
            self.domain = {'xmin':xmin, 'xmax':xmax, 'ymin':ymin, 'ymax':ymax, 
                           'num':len(x), 'int_only': int_only}
        except FileNotFoundError:
            print("Unable to resolve file path or find \'Coord_data.txt\'")
        
    def solveSystem(self):
        A = np.array(self.fillMatrixA())
        B = np.array(self.fillMatrixB())
        self.solution = np.linalg.solve(A,B)
        
    def createPolynomial(self):
        n = len(self.x_values)
        self.polynomial = ''
        for i in range(n, 0, -1):
            self.polynomial += '({0})x^{1}+'.format(self.solution[n-i], str(i-1))
        self.polynomial = self.polynomial.rstrip('+')
        
    def update(self):
        self.extractData()
        self.solveSystem()
        self.createPolynomial()
        
    def fillMatrixA(self):
        matrix = []
        l = len(self.x_values)
        for i in self.x_values:
            row = []
            for j in range(l-1,-1,-1):
                row.append(i**j)
            matrix.append(row)
        return matrix
    
    def fillMatrixB(self):
        matrix = []
        for i in self.y_values:
            matrix.append(i)
        return matrix
    
    def getX(self):
        return self.x_values
    
    def getY(self):
        return self.y_values
    
    def getMatrixA(self):
        return self.fillMatrixA()
    
    def getMatrixB(self):
        return self.fillMatrixB()
    
    def printCoefficients(self):
        print(self.solution)
        
    def printData(self):
        print('X: {0}\nY: {1}\nA: {2}\nB: {3}'.format(self.x_values, 
              self.y_values, self.getMatrixA(),self.fillMatrixB()))
        
    def printPolynomial(self):
        self.update()
        print(self.polynomial)
        
    def demo(self, *ar, **kw):
        if 'reset' in ar:
            self.domain = {'xmin':-5, 'xmax':5, 'ymin':-5, 'ymax':5, 'num':3,
                           'int_only': True}
        elif kw:
            for key in kw:
                if key in self.domain:
                    self.domain[key] = kw[key]
                    
        a = self.domain['xmin']
        b = self.domain['xmax']
        c = self.domain['ymin']
        d = self.domain['ymax']
        n = self.domain['num']
        z = self.domain['int_only']
        
        x_range = b-a
        y_range = d-c
        if z:
            while n > x_range:
                n = int(input('Number exceeds range of domain. '+
                                    'Enter number of points:\n'))
        self.x_values.clear()
        self.y_values.clear()
        if z:
            for i in range(n):
                tmp = random.randint(a, b)
                while tmp in self.x_values:
                    tmp = random.randint(a, b)
                self.x_values.append(tmp)
                self.y_values.append(random.randint(c, d))
        else:
            for i in range(n):
                tmp = random.random()
                while tmp in self.x_values:
                    tmp = random.random()
                self.x_values.append(tmp)
                self.y_values.append(random.random()*y_range + c)
            for i in range(n):
                self.x_values[i] = self.x_values[i]*x_range + a
        data = ''
        for i in range(n):
            data += str(self.x_values[i]) + ' '
            data += str(self.y_values[i]) + '\n'
        f = open('Coord_data.txt', 'w')
        f.write(data)
        f.close()
        self.update()
        
    def printDemoFormat(self):
        print('{\'xmin\':-5, \'xmax\':5, \'ymin\':-5, \'ymax\':5, \'num\':3,' +
                       '\'int_only\': True}')