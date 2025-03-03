import numpy as np
import matplotlib.pyplot as plt

m1 = 4.5 # slope
x = np.arange(-45, 45, 1) # X values ranges from -45 to 45
noise = np.random.normal(0, 4.5, len(x)) # noise
y = m1*x + noise # Y values

# plotting the data
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Visualization')
plt.scatter(x, y)
plt.show()