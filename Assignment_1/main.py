import numpy as np
import matplotlib.pyplot as plt
import time

def dataVisual(x, y, noise):

    # plotting the data
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Data Visualization')
    plt.scatter(x, y+noise, color='red', label='Data Scatter using Noise')
    plt.plot(x, y, color='blue')
    plt.legend()
    plt.show()

def linearApproach(x, y, m1):

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
    plt.plot(m1Guess, m1Errors, color='red', label='Error Graph')
    plt.plot(m1Best, minError, marker='o', markersize=5, color='green', label= f'Best Slope: {m1Best}')
    plt.axhline(m1, color='pink', label=f'True Slope {m1}')
    plt.legend()
    plt.show()

def gradientDescent(x, y, m1):

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
    plt.axhline(m1, color='red', label=f'True Slope {m1}')
    plt.axhline(m1Guess, color='green', label=f'Predicted Slope {m1Guess}')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    m1 = 4.5 # slope
    x = np.arange(-45, 45, 1) # X values ranges from -45 to 45
    noise = np.random.normal(0, 4.5, len(x)) # noise
    y = m1*x # Y values

    dataVisual(x, y, noise)
    linearApproach(x, y, m1)
    gradientDescent(x, y, m1)