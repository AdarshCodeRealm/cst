import random

def die_roll_simulation(num_rolls):
    outcomes = [1, 2, 3, 4, 5, 6]
    roll_results = {outcome: 0 for outcome in outcomes}

    for _ in range(num_rolls):
        roll = random.choice(outcomes)
        roll_results[roll] += 1
    
    probabilities = {outcome: count / num_rolls for outcome, count in roll_results.items()}
    
    return roll_results, probabilities

# Simulate 1000 die rolls
num_rolls = 1000
roll_results, probabilities = die_roll_simulation(num_rolls)

print(f"Roll results: {roll_results}")
print(f"Probabilities: {probabilities}")