import numpy as np
import matplotlib.pyplot as plt
from   utils import *

class Bandit:
    def __init__(self, n_arms):
        self.n_arms = n_arms

        # Memory
        self.successes = np.zeros(n_arms)  # Number of successes (rewards) for each arm
        self.failures = np.zeros(n_arms)   # Number of failures (no rewards) for each arm
        self.n_trials = 0                  # Total number of trials played

    """ @return: Decide arm index """
    def selectArm(self):
        self.n_trials += 1
        return UCB(self.successes, self.failures, self.n_trials, c=4) # Test1 
        return epsilonGreedy(epsilon = 0.1, n=n_arms, calculated = thompson(self.successes, self.failures)) # Test2

    """ Update the Memory """
    def update(self, chosen_arm, reward):
        # Update the successes and failures for the chosen arm
        if reward: self.successes[chosen_arm] += 1
        else: self.failures[chosen_arm] += 1

    def estimation(self):
        # Calculate estimated probabilities for each arm based on successes and failures
        estimated_probs = self.successes / (self.successes + self.failures + 1e-10)  # Avoid division by zero
        total_trials = self.successes + self.failures
        return estimated_probs, total_trials

# Simulation setup: Play with the values.
arm_probabilities = [0.8, 0.2]  # You can add more probabilities for more arms
n_arms = len(arm_probabilities)
n_trials = 1000
bandit = Bandit(n_arms)

# Plot setup
rewards = np.zeros(n_trials)  # Array to store rewards at each trial
choices = np.zeros(n_trials)  # Array to store the chosen arm at each trial
estimations = np.zeros((n_trials, n_arms))  # Array to store estimated probabilities
total_trials_array = np.zeros((n_trials, n_arms))  # Array to store total trials for each arm

# Run the simulation for n trials
for t in range(n_trials):
    
    # 1. Decide the arm
    chosen_arm = bandit.selectArm()  # Bandit decision

    # 2. Try to get Reward 
    reward = (np.random.rand() < arm_probabilities[chosen_arm])  # Simulate the reward from the chosen arm
    bandit.update(chosen_arm, reward)  # Update the algorithm with the outcome

    # 3. Learn
    rewards[t] = reward
    choices[t] = chosen_arm
    estimations[t], total_trials_array[t] = bandit.estimation()  # Store estimated probabilities and total trials

# Final statistics
total_reward = np.sum(rewards)
optimal_choice_percentage = np.mean(choices == arm_probabilities.index(max(arm_probabilities))) * 100 

print(f"Total reward: {int(total_reward):d}")
print(f"Optimal arm chosen {optimal_choice_percentage:.2f}% of the time.")

# Plot the estimated probabilities over time with confidence intervals
plt.figure(figsize=(10, 6))

for i in range(n_arms):
    colors = ['teal', 'orange', 'tomato', 'steelblue']
    plt.plot(np.arange(n_trials), estimations[:, i], label=f'Estimated Probability of Arm {i+1} (True p={arm_probabilities[i]})', color=colors[i])
    plt.axhline(y=arm_probabilities[i], linestyle='dashed', label=f'True Probability of Arm {i+1}', color=colors[i])

plt.title('Multi Arm Bandit', weight='bold')
plt.xlabel('Trial')
plt.ylabel('Estimated Reward Probability')
plt.legend()
plt.grid()
plt.ylim(-0.1, 1.1)  # Set y-axis limits for better visibility
plt.show()
