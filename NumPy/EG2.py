import numpy as np
X = np.array([[1, 2, 3, 4],
[4, 5, 6, 2],
[7, 8, 9, 1],
[2, 5, 1, 5]])

print(X[0:2,1:3])
print()

print(X[0:3,0::2])
print()

print(np.diag(X))
print()

print(X[0:2,0::3])
print()

print(X[0:4,1:3])