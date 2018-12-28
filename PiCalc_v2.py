# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:22:43 2018

@author: Kozmik
"""
import math
import random
import numpy

class PiCalculator:
    def __init__(self, num=1, size=1, radius=0):
        self.num_samples = num      #number of samples
        self.sample_size = size     #size of each sample
        self.radius = radius        #length of circle radius
        self.exp_results = []       #the results of the entire experiment
        self.counts = []            #the number of successes for each sample
        self.sample_calcs = []      #the experimental calculation for each sample
        self.mean = []
        self.variance = []
        self.stdev = []

    def setSampleSize(self, size):
        self.sample_size = size
        
    def setSampleNumber(self, num):
        self.num_samples = num
        
    def setRadius(self, length):
        self.radius = length
        
    def generateSample(self):
        """generates a single sample"""
        sample = []
        for i in range(self.sample_size):
            trial = []
            for j in range(2):
                trial.append((2*random.random()-1)*self.radius)
            sample.append(trial)
        return sample
    
    def runExperiment(self):
        self.exp_results.clear()
        for i in range(self.num_samples):
            self.exp_results.append(self.generateSample())
        self.getExperimentCounts()
        self.getExperimentMeans()
            
    def getExperimentCounts(self):
        self.counts.clear()
        for sample in self.exp_results:
            self.counts.append(self.getSampleCounts(sample))
            
    def getSampleCounts(self, sample):
        counts = 0
        for point in sample:
            summa = 0
            for coordinate in point:
                summa+=coordinate**2
            if math.sqrt(summa) <= self.radius:
                counts+=1
        return counts
            
    def getSampleCalculation(self, sample_loc):
        """calculate the experimental value of pi for a given sample"""
        return 4*(self.counts[sample_loc]/self.sample_size)
        
    def getExperimentMeans(self):
        """calculate the experimental value of pi for every sample in the 
        experiment"""
        self.sample_calcs.clear()
        for i in range(len(self.exp_results)):
            self.sample_calcs.append(self.getSampleCalculation(i))
            
    def getExperimentStatistics(self): 
        stats = (numpy.mean(self.sample_calcs), numpy.var(self.sample_calcs),
                 numpy.std(self.sample_calcs))
        return stats
    
    def getData(self):
        """think about retooling this module for calculating statistics from 
        the interface without changing object values"""
        return self.exp_results
        
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
        stats = self.getExperimentStatistics()
        output += '\nMean: {0}'.format(stats[0])
        output += '\nExperiment Deviation: {0}'.format(stats[2])
#        self.printResults()
        print(output)
        
#    def clearLists(self):
#        self.exp_results.clear()
#        self.sample.clear()
#        self.sample_calcs.clear()

class PiPlot:
    def __init__(self, exp_data):
        self.experiment = exp_data