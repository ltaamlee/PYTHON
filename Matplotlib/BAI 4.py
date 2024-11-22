from matplotlib import pyplot as plt
import numpy as np

category=['Books', 'Food', 'Clothes', 'Office Supplies', 'Machine', 'Sports',
          'Books', 'Food', 'Office Supplies', 'Machine', 'Office Supplies',
          'Machine','Food', 'Clothes']

plt.hist(category, bins=np.arange(len(set(category)) + 1) - 0.5, color='skyblue')

plt.title('Histogram of Categories')
plt.xlabel('Category')
plt.ylabel('Frequency')

plt.show()