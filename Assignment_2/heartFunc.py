import numpy as np
import matplotlib.pyplot as plt

# Class to plot the heart (but do we really need oo for plotting a single heart)
class HeartFunc:
    # Constructor for x and y values
    def __init__(self):
        self.x = np.linspace(-20, 20, 1000)
    # Function to calculate the x and y values
    def heartFunction(self):
        plotX = 16*np.sin(self.x)**3
        plotY = 13*np.cos(self.x) - 5*np.cos(2*self.x) - 2*np.cos(3*self.x) - np.cos(4*self.x)

        return plotX, plotY
    # Function to plot the heart
    def plotHeart(self, plotX, plotY):
        plt.plot(plotX, plotY)
        plt.title("Heart Function")
        plt.show()

if __name__ == "__main__":
    heart = HeartFunc()
    plotX, plotY = heart.heartFunction()
    heart.plotHeart(plotX, plotY)