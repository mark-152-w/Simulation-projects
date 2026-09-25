
import numpy as np
import random as rand
import matplotlib.pyplot as plt

class Road:
    "A class representing traffic on a road"
    
    
    def road_setup(self):
        self.road = np.zeros(self.n)
        maximum = int(self.c*self.n)
        i=1
        while i <= maximum:
            q = rand.randint(0,self.n-1)
            if self.road[q]==0:
                self.road[q] = 1
                i+=1
        
    
    def __init__(self, n, c):
        """Initialise the road list"""
        self.n = n
        self.c = c
        self.Speeds=[]
        self.road_setup()
        self.Places=self.road.copy()
        
    
    def av_speed(self, speed):
        "returns the average speed"
        average_speed=speed/int(self.c*self.n)
        self.Speeds.append(average_speed)
        print(f"average speed = {average_speed}")
    
    def run(self, iterations):
        
        "Checks if the space ahead is empty and space behind is full before moving"
        
        for i in range(iterations):
            
            forward = (self.road==1) & (np.roll(self.road, -1)==0)
            place = np.where(forward)[0]
            self.road[place] = 0
            self.road[(place+1)%len(self.road)]=1
            speed=np.sum(forward)
            self.av_speed(speed)
            self.Places = np.vstack((self.Places, self.road))
            
        
    def steady_state_average(self):
        """
        runs simulation until a steady state is achieved
        returns average speed once this is accomplished
        """
        m=0
        trials = 0
        self.run(3)
        while m<6 and trials < 800:
            self.run(10)
            if self.Speeds[-1] == self.Speeds[-2]:
                m+=1
            trials+=1
        self.steady_state_av_speed = np.mean([self.Speeds[-15:-1]])
    
    def sum_steady_average(self):
        
        """
        takes the steady state average speed for different car densities
        and plots it as a graph
        """
        
        Speeds=[]
        self.c=1/self.n
        c_values=[]
        while self.c<=1:    
            self.road_setup()
            self.steady_state_average()
            Speeds.append( self.steady_state_av_speed)
            c_values.append(self.c)
            self.Speeds=[]
            self.Places=self.road.copy()
            self.c+=(1/self.n)
        plt.figure()
        plt.plot(c_values, Speeds)
        plt.xlabel("car density")
        plt.ylabel("average steady state speed")
        plt.xlim(0,1.01)
        plt.ylim(0,1.01)
        
        
    
    def display(self):
        
        "displays the position of cars over timesteps"
        
        plt.imshow(self.Places, "coolwarm")
        plt.xticks([])
        plt.yticks([])
        plt.xlabel("Road")
        plt.ylabel("Time")
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    n = int(input("number of cells on road = "))
    c = float(input("car density = "))
    iterations = int(input("number of iterations = "))
    traffic = Road(n,c)
    traffic.run(iterations)
    traffic.display()
    traffic.sum_steady_average()
    plt.show()
    
if __name__=="__main__":
    main()