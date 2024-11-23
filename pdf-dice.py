import numpy as np
import matplotlib.pyplot as plt

# Define the number of faces on each die
num_faces = 6

# Initialize an array to store the sum counts
sum_counts = [0] * (num_faces * 2 + 1)

# Calculate the sum counts for all possible outcomes
for die1 in range(1, num_faces + 1):
    for die2 in range(1, num_faces + 1):
        sum_counts[die1 + die2] += 1

# Calculate the total number of possible outcomes
total_outcomes = num_faces * num_faces

# Calculate the probabilities for each sum
probabilities = [count / total_outcomes for count in sum_counts[2:]]

# Define the sums (possible outcomes)
sums = list(range(2, num_faces * 2 + 1))

# Create the bar plot
plt.bar(sums, probabilities, color='skyblue', alpha=0.8)
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Probability Distribution Function of the Sum of Two Dice')
plt.xticks(sums)
plt.show()