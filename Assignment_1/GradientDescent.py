import numpy as np
import matplotlib.pyplot as plt
import time

m1 = 4.5 # slope
x = np.arange(-45, 45, 1) # X values ranges from -45 to 45
noise = np.random.normal(0, 4.5, len(x)) # noise
y = m1*x + noise # Y values

# finding the best slope using gradient descent
currTime = time.time()
m1Guess = np.random.uniform(-10, 10) # random guess for the slope
learningRate = 0.0001 # learning rate
iterations = 1000 # number of iterations
errors = [] # array to store the errors

for _ in range(iterations):
    yGuess = m1Guess*x # prediction
    gradient = -2*np.mean(x * (y - yGuess)) # derivative of the mean squared error
    errors.append(m1Guess)
    m1Guess -= (learningRate*gradient) # updating the slope

print('Time taken:', time.time() - currTime)
print(m1Guess)

plt.plot(errors)
plt.axhline(m1, color='red', label='True Slope')
plt.axhline(m1Guess, color='green', label='Predicted Slope')
plt.legend()
plt.show()