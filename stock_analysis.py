import pandas as pd
df = pd.read_csv('C:/Users/ashok/Downloads/chapter4_assets/chapter4_assets/9_stock_returns_volatility/stock_returns.csv')
df.describe()
df.nvidia_returns.var()
df.reliance_returns.var()
#the higher the variance , the more volatile the dataset will be
#the lower the variance , the lesser volatile or more stable the dataset will be
