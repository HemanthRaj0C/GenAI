import numpy as np
import matplotlib.pyplot as plt
import time

m1 = 4.5 # slope
x = np.arange(-45, 45, 1) # X values ranges from -45 to 45
noise = np.random.normal(0, 4.5, len(x)) # noise
y = m1*x + noise # Y values

# finding the best slope using array
currTime = time.time()
m1Errors = [] # array to store the errors
m1Guess = np.arange(-45, 45, 0.1) # range of guesses for the slope
for m1Pred in m1Guess:
    yGuess = m1Pred*x
    m1Errors.append(np.mean((y - yGuess)**2)) # mean squared error
minError = np.min(m1Errors) # minimum error value
m1Best = m1Guess[(np.argmin(m1Errors))] # best slope using the argmin function
print('Time taken:', time.time() - currTime)

# finding the best slope using dictionary but I didn't use this
newCurrTime = time.time()
newM1 = {}
for i in m1Guess:
    newM1[i] = np.mean((y - i*x)**2)
bestNewM1 = (min(newM1, key=newM1.get))
print('Time taken:', time.time() - newCurrTime)

print(bestNewM1, m1Best)

# plotting the data
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Visualization')
plt.plot(m1Guess, m1Errors, color='red', label='Error')
plt.plot(m1Best, minError, marker='o', markersize=5, color='pink', label= f'Best Slope: {m1Best}')
plt.legend()
plt.show()