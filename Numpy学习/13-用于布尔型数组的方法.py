import numpy as np

# sum()
arr = np.random.randn(100)
print((arr > 0).sum())

# any()
bools = np.array([False, True, True, False])
print(bools.any())
print(bools.all())
