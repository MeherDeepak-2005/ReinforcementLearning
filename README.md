# EpsilonGreddy
Epsilon Greedy Algorithm implemented in python from scratch using Numpy.




Epsilon Greedy Algorithm has following advantages:
  Balances between Explore and Exploit.
  Enchances Greedy Algorithm by choosing actions at a random at a small probability, represented by Epsilon ε
  
# Prerequisites
### Greedy Algorithm to better understand the importance of Epsilon Greedy.
### Advanced level python programming language understanding.

# The Greedy Algorithm
* Multi-armed bandit problem
* Always picking the bandit with the highest probability
### psuedocode
```python
while True:
  chosen_bandit = argmax(bandit means collected)
  reward = play bandit j and collect reward
  bandits[j].update_mean(reward)
```


# Pseudocode for epsilon greedy
* For multi-armed bandit problem
```python
while True:
  epsilon = 0.2
  randomProb = random number in [0,1]
  if randomProb < epsilon:
    j = choose a random bandit
  else:
    j = argmax(means of bandits)
  x = perform action on bandit j and get reward
  bandits[j].update_mean(x)
```
