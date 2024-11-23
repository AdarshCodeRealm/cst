#AUTOCORRELATION COEEFIENT
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

desired_covariance = 0.02
std_dev_x = 1.00
std_dev_y = 1.00
np.random.seed(0)

# Create the covariance matrix
cov_matrix = np.array([[std_dev_x**2, desired_covariance],
                        [desired_covariance, std_dev_y**2]])

# Generate data with specified covariance
data = np.random.multivariate_normal(mean=[0, 0], cov=cov_matrix, size=60)
x, y = data[:, 0], data[:, 1]

# Calculate covariance and correlation coefficient
covariance_matrix = np.cov(x, y)
correlation_coeff, _ = pearsonr(x, y)

# Create the scatter plot with annotations
plt.figure(figsize=(7, 5))
plt.scatter(x, y, label=f'Correlation: {correlation_coeff:.2f}', alpha=0.6)
plt.text(0.1, 0.9, f'Covariance: {covariance_matrix[0, 1]:.2f}',
         transform=plt.gca().transAxes)
plt.text(0.1, 0.85, f'Correlation Coefficient: {correlation_coeff:.2f}',
         transform=plt.gca().transAxes)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.title("Scatter Plot with Covariance")
plt.show()