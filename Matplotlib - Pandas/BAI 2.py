from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv('chipotle.tsv',sep='\t')

print("Cac san pham co gia hon 10$ : ")
filtered=df[df['item_price'].str.replace('$','').astype(float)>10]
unique=filtered.drop_duplicates(subset='item_name')
print(unique[['item_name','item_price']])
print()

print("Sap xep san pham theo ten : ")
sorted_items=df['item_name'].sort_values()
print(sorted_items)
print()

print("San pham co gia cao nhat : ")
max_price_items= df.loc[df['item_price'].str.replace('$', '').astype(float).idxmax()]
print(max_price_items)
print()

print('So lan xuat hien cua san pham Veggie Salad Bowl tren tong so luong don dat hang: ')
data=df[df['item_name']=="Veggie Salad Bowl"].groupby('item_name').agg({'order_id':'count','quantity':'sum'})
print(data.head())

#Histogram
data=df.groupby('item_name')['quantity'].sum().nlargest(5)
data.plot.bar()
plt.show()

#Scatter
data=df.groupby('order_id')['quantity'].sum().to_frame()
plt.scatter(data.index, data.values, color="purple", alpha=0.5)
plt.show()