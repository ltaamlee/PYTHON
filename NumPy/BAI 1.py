import numpy as np
# row,col=2,4
# a=[[[0]*row]*col]
# print(a)

row,col=2,4
a=[[0 for i in range(row)] for i in range(col)]
print(a)

a=np.zeros((2,4))
print(a)
