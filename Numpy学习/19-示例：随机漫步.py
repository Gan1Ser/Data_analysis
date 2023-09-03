import random
import numpy as np
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
plt.show()

nsteps = 1000
draws = np.random.randint(0, 2, size=10)
print(draws)
steps = np.where(draws > 0, -1, 1)
print(steps)
walk = steps.cumsum()

nwalks = 50
nsteps = 10
draws = np.random.randint(0,2,size=(nwalks, nsteps)) # 0 或者 1, 5000个1000步的随机漫步过程

steps = np.where(draws > 0, -1, 1)
walks = steps.cumsum(1)
print(walks)

hits30 = (np.abs(walks) >= 3).any(1)
print('hits30')
print(hits30)
print(hits30.sum())

crossing_times = (np.abs(walks[hits30]) >= 3).argmax(1)
print(crossing_times)
