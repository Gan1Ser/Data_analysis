import numpy as np
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))
arr1 = np.arange(11)
np.savez('array_archive.npz', a=arr, b=arr1)
arch = np.load("array_archive.npz")
print(arch['b'])

np.savez_compressed('arrays_compressed.npz', a=arr, b=arr1)
arch = np.load("arrays_compressed.npz")
print(arch["b"])