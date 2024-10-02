# Thompson Sampling
Thompson Sampling is a probabilistic algorithm used in the multi-armed bandit problem to balance exploration (trying different options) and exploitation (choosing the best-known option) by modeling uncertainty in the rewards. It uses Bayesian inference to estimate the likelihood that each option (or "arm") is the best one based on past observations, and then it chooses arms by sampling from these likelihood estimates.

### How Thompson Sampling Works:
1. **Bayesian Inference**: Each arm is modeled with a probability distribution that represents the uncertainty about the true reward it will provide. Initially, this distribution is broad because little is known about each arm.

2. **Sampling from the Distributions**: For each arm, the algorithm samples a value from its probability distribution. These samples reflect the potential reward each arm could give based on the current belief.

3. **Select the Arm with the Highest Sample**: After sampling, the arm with the highest sampled value is selected for that round. This allows Thompson Sampling to explore different arms while still leaning toward the arms that have shown better rewards in the past.

4. **Update the Distribution**: After receiving a reward from the selected arm, the algorithm updates the probability distribution for that arm based on the observed outcome. This process is typically done using conjugate priors, like the Beta distribution for binary rewards (success/failure).

### Key Concepts:
- **Bayesian Updating**: Thompson Sampling relies on Bayesian updating, meaning it continuously refines its beliefs about each arm’s probability of success based on the outcomes observed over time.
- **Uncertainty and Sampling**: Unlike greedy algorithms that pick the best arm deterministically, Thompson Sampling samples from probability distributions, which naturally balances exploration (trying uncertain arms) and exploitation (choosing arms with high expected rewards).
- **Beta Distribution**: In cases where the reward is binary (e.g., success/failure), the Beta distribution is commonly used. The distribution is updated based on the number of successes and failures observed from each arm.

### Example:
Imagine you have three slot machines, and each machine has an unknown probability of giving a reward. Thompson Sampling begins by assuming that all machines have an equal chance of being the best. It pulls each machine a few times, updating its belief about each machine’s reward probability based on successes (rewards) and failures (no rewards). For each round:
- It samples from the Beta distribution for each machine, which gives it an estimate of the reward probability for that machine.
- It chooses the machine with the highest sampled reward probability.
- After observing the outcome, it updates the distribution for the chosen machine.

### Advantages:
- **Efficient Exploration**: Since Thompson Sampling naturally samples more from uncertain arms early on and shifts to more exploitation over time, it effectively balances exploration and exploitation without needing to specify a fixed exploration rate (like epsilon in Epsilon-Greedy).
- **Dynamic Adaptation**: The algorithm adapts its exploration strategy based on how uncertain it is about the arms, which makes it efficient in various settings.

Thompson Sampling is widely used in applications like online advertising, recommendation systems, and clinical trials, where it’s important to explore new strategies but also make decisions based on the best available evidence.
