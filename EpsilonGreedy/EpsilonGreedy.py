import matplotlib.pyplot as plt
import numpy as np


# Number of times we are gonna run our program.
Epochs = 1000000 # Optimal would be minimum 1000 trails or greater if you wanna see results.
# Pre defining bandit probabilities to see how the algorithm changes the program's behavior.
BD_Prob = [0.2,0.5,0.75]
# Defininig ε (epsilon)
epsilon = 0.1

class Bandit:
  def __init__(self,p):
    self.p = p
    self.estimate_p = 0
    self.N = 0 # Number of samples we have collected by running our program.

  def pull(self):
    return np.random.random() < self.p
    # Returns true or false at random rate of self.p value. Nothing else.

  def update(self,x):
    self.N += 1
    self.estimate_p = ((self.N-1)*self.estimate_p + x)/self.N
  
def model():
  # Converting each bandit into Type of Class Bandit so that we can access the class's functions.
  bandits = [Bandit(p) for p in BD_Prob]
  rewards = np.zeros(Epochs)
  num_times_explored = 0
  num_times_exploited = 0
  num_optimal = 0
  optimal_j = np.argmax([b.estimate_p for b in bandits])
  # Optimal J would be 2. since we already defined the probabilities.
  for i in range(Epochs):
    # Epsilon Greedy Algorithm
    if np.random.random() < epsilon:
      num_times_explored += 1
      j = np.random.randint(len(bandits))
    else:
      num_times_exploited += 1
      j = np.argmax([b.estimate_p for b in bandits])
    if j == optimal_j:
      num_optimal += 1
      # Checking if the optimal bandit has changed or not.
      # Can be helpful if result isn't satisfactory and want to change Epsilon value accordingly.

    # Updating the win probabilty of the selected bandit.
    x = bandits[j].pull()
    rewards[i] = x
    bandits[j].update(x)

  for b in bandits:
    print(f"Mean Estimate: {b.estimate_p}")

  print(f"Overall Win Rate: {rewards.sum()/Epochs}")
  cumulative_rewards = np.cumsum(rewards)
  plt.title('Epsilon Greedy')
  win_rates = cumulative_rewards / (np.arange(Epochs)+1)
  plt.plot(win_rates)
  plt.plot(np.ones(Epochs)*np.max(BD_Prob))
  plt.show()
    
if __name__ == '__main__':
  model()


