import numpy as np
from   scipy.stats import beta

def thompson(positive, negative):
    size = len(positive)
    sampled_values = [beta.rvs(a=1 + positive[i], b=1 + negative[i]) for i in range(size)] # Sample from the Beta distribution for each element
    return np.argmax(sampled_values)    # Choose the element with the highest sampled value

def epsilonGreedy(epsilon:float, n:int, calculated) -> int:
    if np.random.rand() < epsilon: 
        return np.random.randint(0, n)  # Explore: Random element.
    else: 
        return calculated  # Exploit: Select index based on calculation.

def UCB(positive, negative, total, c=2):
    """Calculate UCB values for each element."""
    size = len(positive)

    ucb_values = np.zeros(size)
    for i in range(size):
        if positive[i] + negative[i] == 0: 
            ucb_values[i] = float('inf')  # Assign infinite value to untried arms
        else:
            ucb_values[i] = (positive[i] / (positive[i] + negative[i])) + \
                             c * np.sqrt(2 * np.log(total) / (positive[i] + negative[i]))
    return np.argmax(ucb_values)
