import pandas as pd
import numpy as np

s1=pd.Series(np.random.randint(1,5,100))
s2=pd.Series(np.random.randint(1,4,100))
s3=pd.Series(np.random.randint(10000,30000,100))

df=pd.concat([s1,s2,s3], axis=1)

df.columns=['bedrs', 'bathrs', 'price_sqr_meter']

df['bigcolumn']=df['bedrs']+df['bathrs']+df['price_sqr_meter']

df.reset_index(drop=True, inplace=True)

print(df)
