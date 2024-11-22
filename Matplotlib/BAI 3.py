from matplotlib import pyplot as plt 
import numpy as np

category=['Books', 'Food', 'Clothes', 'Office Supplies', 'Machine', 'Sports']
sales=[3500, 2000, 1800, 2200, 4500, 3100]

x=np.arange(len(category))

plt.bar(x,sales,color="skyblue")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(x,category)
plt.show()