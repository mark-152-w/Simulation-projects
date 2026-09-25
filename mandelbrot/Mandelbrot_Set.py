import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot_Set():

    "creates a list"
    def __init__(self, real_min, real_max, im_min, im_max, step):
        self.real_min = real_min
        self.real_max = real_max
        self.im_min = im_min
        self.im_max = im_max
        self.step = step
        
    "calculates which numbers fall into the mandelbrot set"
    def calc(self):
        
        "creates grid of numbers"
        X = np.arange(self.real_min, self.real_max, self.step)
        Y = np.arange(self.im_min, self.im_max, self.step)
        XX, YY = np.meshgrid(X, Y)
        self.Z = XX + 1j*YY
        self.Grid = np.zeros(self.Z.shape)
        
        for i in range(len(Y)):
            for j in range(len(X)):
                n=1
                c = self.Z[i][j]
                z=0
                while n < 256 and abs(z) < 2:
                    z = z**2 + c
                    n+=1
                self.Grid[i][j]=n
                    
    
    "displays the results of this calculation"
    def display(self):
        left = self.real_min
        right = self.real_max
        bottom = self.im_min
        top = self.im_max
        plt.imshow(self.Grid, extent = (left, right, bottom, top))
        plt.colorbar()
        plt.xlabel("Re")
        plt.ylabel("Im")
        plt.show()
        
        
        
    
    
    
    
    
    
    
    
    
    