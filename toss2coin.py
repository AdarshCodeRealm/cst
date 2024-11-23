import random

def coin_toss_simulation(num_tosses):
    heads = 0
    tails = 0
    
    for _ in range(num_tosses):
        if random.choice(['heads', 'tails']) == 'heads':
            heads += 1
        else:
            tails += 1
    
    prob_heads = heads / num_tosses
    prob_tails = tails / num_tosses
    
    return prob_heads, prob_tails

# Simulate 1000 coin tosses
num_tosses = 1000
prob_heads, prob_tails = coin_toss_simulation(num_tosses)

print(f"Probability of heads: {prob_heads}")
print(f"Probability of tails: {prob_tails}")