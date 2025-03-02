import numpy as np
import matplotlib.pyplot as plt

xVal = np.linspace(-5, 5, 200)
m1Val = 4.5
noiseN = np.random.normal(0, 1, size=xVal.shape)  # Gaussian noise N(0,1)
y = m1Val * xVal + noiseN

plt.scatter(xVal, y, label="Data Vizualization", color="red", alpha=0.5)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Dataset Visualization")
plt.legend()
plt.show()