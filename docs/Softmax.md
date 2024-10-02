# Softmax
Softmax is a mathematical function that converts a vector of raw scores (logits) into probabilities. It is commonly used in machine learning, particularly in classification tasks, to produce a probability distribution over multiple classes. The softmax function ensures that the output values are non-negative and sum to one, making them interpretable as probabilities.
Definition

Given a vector z=[z1,z2,…,zn]z=[z1​,z2​,…,zn​], the softmax function is defined as follows:
P(ai)=ezi∑j=1nezj
P(ai​)=∑j=1n​ezj​ezi​​

where:

    P(ai)P(ai​) is the probability of class ii,
    zizi​ is the raw score (logit) for class ii,
    ee is the base of the natural logarithm,
    The denominator is the sum of exponentials of all class scores, ensuring that the probabilities sum to one.

### Properties

    Range: The output of the softmax function is in the range (0,1)(0,1) for each class.
    Normalization: The sum of all output probabilities equals 1:
    ∑i=1nP(ai)=1
    i=1∑n​P(ai​)=1
    Exponentiation: The use of exponentials ensures that larger logits result in higher probabilities, while smaller logits lead to probabilities closer to zero.

### Interpretation

    Probability Distribution: The softmax function allows for interpreting the output of a model as a probability distribution over different classes, which is particularly useful in multi-class classification problems.
    Sensitivity to Differences: Softmax amplifies differences between the input logits. If one logit is much larger than the others, the softmax output will heavily favor that class.

### Applications

    Multiclass Classification: Softmax is widely used in neural networks as the activation function for the output layer in multiclass classification tasks.
    Reinforcement Learning: In the context of algorithms like the Gradient Bandit Algorithm, softmax can be used to select actions based on their preferences, enabling exploration of various actions while favoring those that are more likely to yield higher rewards.
    Natural Language Processing: Softmax is often used in models like language models to predict the probability distribution of the next word in a sequence.

### Example

Consider three classes with logits [2.0,1.0,0.1][2.0,1.0,0.1]. The softmax probabilities can be calculated as follows:

    Calculate the exponentials:
    e2.0≈7.39,e1.0≈2.72,e0.1≈1.11
    e2.0≈7.39,e1.0≈2.72,e0.1≈1.11

    Compute the sum of exponentials:
    Sum≈7.39+2.72+1.11≈11.22
    Sum≈7.39+2.72+1.11≈11.22

    Calculate the probabilities:
    P(a1)=7.3911.22≈0.66,P(a2)=2.7211.22≈0.24,P(a3)=1.1111.22≈0.10
    P(a1​)=11.227.39​≈0.66,P(a2​)=11.222.72​≈0.24,P(a3​)=11.221.11​≈0.10

### Summary

The softmax function is a fundamental tool in machine learning for transforming logits into probabilities, allowing models to make decisions based on the likelihood of different classes. Its properties of normalization and sensitivity make it particularly useful in various applications, especially in neural networks and reinforcement learning algorithms.