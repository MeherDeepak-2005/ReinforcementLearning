# Optimisitc Initial Value
* Another way to solve the multi-arm bandit problem in Machine learning

## How is it different from Epsilon Greedy ?
* Epsilon Greedy chooses a random action at a small probability represented by Epsilon.
* Optimisitic Initial Value doesn't use any sort of probability for choosing a random action.
* Optimistic Initial Value will initialize mean to very large value. It uses greedy method to choose bandit.
* This helps the program choose the highest win rate bandit until it's win rate drops below than others. 

### Difference in code from Epsilon Greedy
```python
class Bandit:
  def __init__(self,p):
    self.p = p
    self.estimate_p = 10 #Very high value
    self.N = 1

  # Greedy algorithm
  def model():
    for i in range(epochs):
      j = np.argmax([b.estimate_p for b in bandits])

```