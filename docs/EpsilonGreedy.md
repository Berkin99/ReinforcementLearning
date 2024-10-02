# Epsilon Greedy
Epsilon-Greedy is a simple yet effective algorithm used in the multi-armed bandit problem to balance exploration (trying out less familiar options) and exploitation (choosing the best-known option). In this context, you have multiple options, often referred to as "arms" (like in a slot machine), and each arm gives a reward when selected. The goal is to maximize the total reward over time.

1. **Exploitation (Choosing the Best Option)**: With probability \(1 - \epsilon\), the algorithm selects the arm that has the highest average reward based on past trials. This means it "exploits" the best option it has found so far.

2. **Exploration (Trying New Options)**: With a small probability \(\epsilon\) (where \(\epsilon\) is typically a small value like 0.1), the algorithm chooses a random arm. This allows the algorithm to "explore" other options, which might turn out to be better in the long run.

### Key Concepts:
- **Epsilon (\(\epsilon\))**: This is a parameter that determines how often the algorithm should explore new options. A higher \(\epsilon\) means more exploration, and a lower \(\epsilon\) means more exploitation.
- **Balancing**: By alternating between exploitation and exploration, the algorithm avoids getting stuck in a suboptimal solution while still focusing on the best-known arms.

### Example:
Imagine you are at a casino with three slot machines, and you want to maximize your total winnings. Initially, you don’t know which machine is the best. With Epsilon-Greedy, you might:
- Play the machine that has given you the highest average payout 90% of the time (exploitation).
- But 10% of the time, you’ll randomly choose one of the three machines (exploration), to make sure you’re not missing out on a potentially better one.

This approach helps strike a balance between trying new things and sticking with the known best option.

