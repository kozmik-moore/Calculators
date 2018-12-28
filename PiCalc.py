# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:22:43 2018

@author: Kozmik
"""
import math
import random
import numpy

class PiCalculator:
    def __init__(self, num=0, size=0, radius=0, dims=0):
        self.num_samples = num      #number of samples
        self.sample_size = size     #size of each sample
        self.radius = radius        #length of circel radius
        self.dimensions = dims      #array dimensions (of space)
        """only works in 2D space because of the ratio of the area of a circle 
        and a square (i.e. 1D space has ratio 1, 2D has ratio pi, 3D has ratio
        4/3*pi,..."""
        self.sample = []            #the results of a single experiment
        self.exp_results = []
        self.mean = 0
        self.variance = 0
        self.stdev = 0
        self.sample_means = []

    def setSampleSize(self, size):
        self.sample_size = size
        
    def setSampleNumber(self, num):
        self.num_samples = num
        
    def setDimensions(self, dims):
        self.dimensions = dims
        
    def setRadius(self, length):
        self.radius = length
    
    def runExperiment(self):
        self.exp_results.clear()
        for i in range(self.num_samples):
            self.generateSample()
            self.exp_results.append(self.getSampleCounts())
        
    def generateSample(self):
        self.sample.clear()
        for i in range(self.sample_size):
            points = []
            for j in range(self.dimensions):
                points.append((2*random.random()-1)*self.radius)
            self.sample.append(points)
            
    def getSampleCounts(self):
        counts = 0
        for point in self.sample:
            summa = 0
            for coordinate in point:
                summa+=coordinate**2
            if math.sqrt(summa) < self.radius:
                counts+=1
        return counts
            
    def getSampleMeans(self):
        self.sample_means.clear()
        for sample in self.exp_results:
            self.sample_means.append((2**self.dimensions)*sample/self.sample_size)
            
    def getStatistics(self):
        self.getSampleMeans()
        self.mean = numpy.mean(self.sample_means)
        self.variance = numpy.var(self.sample_means)
        self.stdev = numpy.std(self.sample_means)
        
    def printResults(self):
        output = ''
        output += '\nNumber of samples: {0}'.format(self.num_samples)
        output += '\nSample size: {0}'.format(self.sample_size)
        output += '\nMean: {0}'.format(self.mean)
        output += '\nDeviation: {0}'.format(self.stdev)
        print(output)
        
    def runAndPrint(self):
        output = ''
        output += '\nNumber of samples: {0}'.format(self.num_samples)
        output += '\nSample size: {0}'.format(self.sample_size)
        self.runExperiment()
        self.getStatistics()
        output += '\nMean: {0}'.format(self.mean)
        output += '\nExperiment Deviation: {0}'.format(self.stdev)
#        self.printResults()
        print(output)
        
#    def clearLists(self):
#        self.exp_results.clear()
#        self.sample.clear()
#        self.sample_means.clear()

class PiPlot:
    def __init__(self, exp):
        self.experiment = exp