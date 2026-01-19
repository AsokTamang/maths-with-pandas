import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/ashok/Downloads/chapter6_assets/chapter6_assets/5_z_score/heights_with_outliers.csv")
m=df.height.mean()
s=df.height.std()
print('The mean is:', m)
print('The standard deviation is:', s)
df['Z-Score'] = (df['height'] - m) / s
#as the valid z-score range is between -3 to 3
outliers = df[(df['Z-Score']<-3)|(df['Z-Score']>3)]
print('The outliers based on z-score is:' , outliers)
