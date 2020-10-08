import numpy as np

class Map:
    def __init__(self, str, rows, cols):
        self.fileName = str
        self.size = [rows,cols]
        self.map = self.readFile(self.fileName)
        
            
    def readFile(self, fileName):
        f = open(fileName, 'r')
        m = np.empty((self.size[0], self.size[1]), dtype = 'S1') #creates empty array to place map in
        r = 0
        c = 0
        for line in f:
            for ch in line.strip():
                m[r,c] = ch
                c += 1
            r += 1
            c = 0
            
        return m