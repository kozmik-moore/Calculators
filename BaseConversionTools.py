##import math
import numpy as np

class Toolbox:    
    def __init__(self):
#        self.BASE40 = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i',
#                       'j','k','l','m','n','o','p','q','r','s','t','u','v','w',
#                       'x','y','z','aa','bb','cc','dd']
        self.baselib1 = []
        self.baselib2 = []
        self.old = 10
        self.new = 10
        self.setBases(10,10)

    def setBases(self, old=None, new=None):
        change = [None,None]
        if old:
            if old <=36:
                self.old = old
                change[0] = old
            else:
                print("Old base is too large!\n")
        if new:
            if new <= 36:
                self.new = new
                change[1] = new
            else:
                print("New base is too large!\n")
        if change[0] or change[1]:
            self.setBaseLibraries(change[0], change[1])
            
    def getOldBase(self):
        return self.baselib1
    
    def getNewBase(self):
        return self.baselib2
            
    def setBaseLibraries(self, old=None, new=None):
        if old:
            self.baselib1 = self.makeCryptBase(old)
        if new:
            self.baselib1 = self.makeCryptBase(new)
            
    def __print__(self):
        print("Base 1 is %d and base 2 is %d.", self.old, self.new)
            
    def convertValue(self, value):
        new = value
        digit = 0
        string = ""
        if self.old > self.new:
            while new is not 0:
                digit = new % self.new
                string = str(digit) + string
                new //= self.new
        return int(string)
    
    def makeCryptBase(self, size):
        base10 = ['0','1','2','3','4','5','6','7','8','9']
        ref = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
               'q','r','s','t','u','v','w','x','y','z']
#        base = ''
        if size <= 10:
            return base10[0:size]
        elif size <=36:
            return base10+ref[0:(size-10)]
#        base = base10+ref
#        i = (size-36)//size
#        j = (size-36)%size
#        for x in range(i):
#            for y in range(j):
    
    def getInput(self):
        key = input("Input a string:")
        key = key.replace(' ', '')
        key = list(key)
        excess = len(key)%4
        for i in range(excess):
            key.pop(-1)
        tmp = []
        while len(key) > 0:
            x=key.pop(0)
            y=key.pop(0)
            f=(self.baselib1.index(x),self.baselib1.index(y))
            x=key.pop(0)
            y=key.pop(0)
            s=(self.baselib1.index(x),self.baselib1.index(y))
            item = (f,s)
            tmp.append(np.array(item))
        return tmp
            
    def generateMatrices(self, arr):
        tmp = []
        for item in range(len(arr)-1):
            tmp.append(arr[item]@(arr[-1]))
        return tmp
    
    def generateString(self, arr):
        string = ''
        modulus = len(self.baselib1)
        for matrix in (arr):
            for x in range(2):
                for y in range(2):
                    string+=self.baselib1[int(matrix[x,y])%modulus]
        return string
    
    def simpCrypt(self, num, lib):
        tmp = num%len(lib)
        return str(lib[tmp])