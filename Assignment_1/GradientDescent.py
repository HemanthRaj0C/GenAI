import numpy as np
import matplotlib.pyplot as plt

xVal = np.linspace(-5, 5, 200)
m1Val = 4.5 
noiseN = np.random.normal(0, 1, size=xVal.shape)  # Gaussian noise
y = m1Val * xVal + noiseN

# Gradient Descent Parameters
m1 = np.random.randn() # Random initialization
learningRate = 0.01
numIterations = 100000
m1History = []

for i in range(numIterations):
    yPred = m1 * xVal
    gradient = -2 * np.mean(xVal * (y - yPred)) # Derivative of MSE
    stepSize = learningRate * gradient
    m1 -= stepSize
    m1History.append(m1)

plt.plot(m1History, label="m1 Values", color="blue")
plt.axhline(y=m1Val, color='r', linestyle='--', label="Actaul m1")
plt.axhline(y=m1, color='g', linestyle='--', label="Estimated m1")
plt.xlabel("Iterations")
plt.ylabel("m1 Value")
plt.title("Gradient Descent")
plt.legend()
plt.show()

print(f"Estimated m1: {m1:.4f}")
