#correlation and covarience matrix 
import numpy as np
import pandas as pd

# Parameters
fs = 100  # Sampling frequency in Hz
tau = 1
# Duration in seconds
N = int(fs * tau)  # Total number of samples

# Generate synthetic data (3 features)
np.random.seed(0)  # For reproducibility
data_points = np.random.rand(N, 3)  # Random data for 3 features

# Convert the NumPy array to a Pandas DataFrame
df = pd.DataFrame(data_points, columns=['Feature_1', 'Feature_2', 'Feature_3'])

# Calculate the covariance matrix using Pandas
cov_matrix = df.cov()
print("Covariance Matrix:")
print(cov_matrix)

# Calculate the correlation coefficient matrix using Pandas
corr_matrix = df.corr()
print("\nCorrelation Coefficient Matrix:")
print(corr_matrix)