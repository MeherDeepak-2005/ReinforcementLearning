# How to implement UCB1 algorithm
import matplotlib.pyplot as plt
import numpy as np

banditProbs = [0.34,0.694,0.8028]
Epochs = 10000

class Bandit:
  def __init__(self,p):
    #Win rate
    self.p = p
    self.p_estimate = 0 # Sample mean
    self.N = 3

  def pull(self):
    # More winrate more rewards.
    return np.random.random() < self.p
  
  def update(self,x):
    self.N += 1
    self.p_estimate = ((self.N-1)*self.p_estimate + x)/self.N
  

def ucb(mean,n,nj):
  return mean + np.sqrt(2*np.log(n)/nj)
  
def model():
  bandits = [Bandit(p) for p in banditProbs]
  rewards = np.zeros(Epochs)
  total_plays = 0
  # Initialization: Play each bandit once so that n and nj are not zero.
  for j in range(len(bandits)):
    x = bandits[j].pull()
    total_plays += 1
    bandits[j].update(x)
  for i in range(Epochs):
    j = np.argmax([ucb(b.p_estimate,total_plays,b.N) for b in bandits])
    x = bandits[j].pull()
    total_plays += 1
    bandits[j].update(x)
    rewards[i] = x
  for b in bandits:
      print(f"Mean Estimate: {b.p_estimate}")
  cumulative_average = np.cumsum(rewards)/(np.arange(Epochs)+1)
  win_rates = cumulative_average / (np.arange(Epochs)+1)
  plt.plot(win_rates)
  plt.plot(np.ones(Epochs)*np.max(banditProbs))
  plt.xscale('log')
  plt.show()
      
    
if __name__ == "__main__":
  model()