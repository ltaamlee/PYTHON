from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv("Churn_Modelling.csv")

score=df.groupby('Geography')['CreditScore'].mean()

df['Age_group'] = pd.qcut(df['Age'], q=5, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])
print(df['Age_group'].value_counts())

x=df['Age_group'].value_counts()

plt.bar(x.index, x.values, color='skyblue')

plt.title('Số lượng khách hàng theo nhóm độ tuổi', fontsize=14)
plt.xlabel('Nhóm độ tuổi', fontsize=12)
plt.ylabel('Số lượng khách hàng', fontsize=12)

plt.show()
