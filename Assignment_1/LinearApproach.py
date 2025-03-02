import numpy as np
import matplotlib.pyplot as plt

xVal = np.linspace(-5, 5, 200)
m1Val = 4.5
noiseN = np.random.normal(0, 1, size=xVal.shape)  # Gaussian noise N(0,1)
y = m1Val * xVal + noiseN

# linear search for the best m1 value
m1Range = np.linspace(-50, 50, 100)
errors = []  # Store MSE for each m1

for m1 in m1Range:
    yPred = m1 * xVal  # ignore the constant term (y = mx + c)
    error = np.mean((y - yPred) ** 2)  # MSE
    errors.append(error)

# best m1 (minimum error)
m1Best = m1Range[np.argmin(errors)]
yBest = m1Best * xVal

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # to show both graphs side by side

# Subplot 1: Data visualization with best-fit line
axes[0].scatter(xVal, y, label="Data Visualization", color="red", alpha=0.5)
axes[0].plot(xVal, yBest, label=f"Best Fit Line (m1={m1Best:.2f})", color="blue", linewidth=2)
axes[0].set_xlabel("X values")
axes[0].set_ylabel("Y values")
axes[0].set_title("Linear Regression Best Fit")
axes[0].legend()

# Subplot 2: MSE vs. m1 values
axes[1].plot(m1Range, errors, color="purple", linewidth=2)
axes[1].axvline(m1Best, color='green', linestyle='dashed', label=f"Minima at m1={m1Best:.2f}")
axes[1].set_xlabel("m1 values")
axes[1].set_ylabel("MSE (Error)")
axes[1].set_title("Error Function vs. m1")
axes[1].legend()

# Adjust layout and display both graphs side by side
plt.tight_layout()
plt.show()

# Print the best m1 value
print(f"Best m1 value found: {m1Best:.4f}")
