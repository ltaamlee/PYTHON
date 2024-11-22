from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv('u.user',sep='|')

print("Do tuoi trung binh cua moi nghe nghiep : ")
avg_age=df.groupby('occupation')['age'].mean()
print(avg_age)
print()

print("Ty le nam tren moi nghe va sap xep tu cap den thap : ")
ratio=df.groupby('occupation')['age'].mean().sort_values(ascending=False)
print(ratio)
print()

print("Do tuoi nho nhat va lon nhat cua moi nghe nghiep : ")
age_min_max=df.groupby('occupation')['age'].agg(['min', 'max'])
print(age_min_max)
print()

print("Ti le phan tram nam-nu moi nghe nghiep : ")
count_gen=df.groupby(['occupation','gender']).size().unstack()
ratio_gen=(count_gen.div(count_gen.sum(axis=1), axis=0)) * 100
print(ratio_gen)