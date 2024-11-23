#joint pdf
import itertools
import matplotlib.pyplot as plt
import random

# Define number of tosses
n_tosses = 50

# Define coin outcomes
coin_outcomes = ["H", "T"]

# Generate all possible outcomes (list of tuples)
all_outcomes = list(itertools.product(coin_outcomes, repeat=3))

# Initialize dictionary to store outcome counts
outcome_counts = {outcome: 0 for outcome in all_outcomes}

# Simulate coin tosses and update outcome counts
for _ in range(n_tosses):
    toss_result = tuple(random.choice(coin_outcomes) for _ in range(3))
    outcome_counts[toss_result] += 1

# Calculate probabilities from counts
probabilities = [count / n_tosses for count in outcome_counts.values()]

# Create the bar plot
plt.bar(range(len(all_outcomes)), probabilities, color='skyblue', alpha=0.6)

# Set labels and title
plt.xlabel('Outcome (0, 1, 2, 3 Heads)')
plt.ylabel('Probability')
plt.title('Probability Distribution of Tossing Three Coins 50 Times')

# Rotate x-axis tick labels for better readability
plt.xticks(range(len(all_outcomes)), ["".join(outcome) for outcome in all_outcomes], rotation=45)

plt.show()