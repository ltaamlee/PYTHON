import numpy as np

A=np.random.randint(1,21,2352)

B=np.random.randint(-20,0,2352)

print(A.tolist())
print(B)

print(A.shape)
print(B.shape)

C=A.reshape(28,28,3)

D=B.reshape(28,28,3)

E=np.concatenate((C,D),axis=1)
print(E.shape) #noi theo dong

F=np.stack([C,D])
print(F.shape)

G=np.hstack([C,D])
print(G.shape)