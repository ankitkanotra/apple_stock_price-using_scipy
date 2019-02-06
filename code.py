import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\Hp\PycharmProjects\analysis\HistoricalQuotes (1).csv',parse_dates=["date"],index_col="date")
df
df.close.mean()
df["2019-01"].close.mean()
import matplotlib.pyplot as plt
plt.scatter(df.open,df.close)
%matplotlib inline
plt.scatter(df.open,df.close)
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(df[['close','volume']],df.open)
reg.predict([[165,36450278]])
