import numpy as np
a=np.random.randint(low=-5, high=5, size=6)
print(a)

l=a[np.where(a>0)]
print("Cac phan tu lon hon 0 :",l)
