import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter6_assets/chapter6_assets/3_normal_distribution/heights.csv")
sns.histplot(df,kde=True)
mean =round(df.height.mean(),2)
st_dev=round(df.height.std(),2)
plt.axvline(mean,color='black',linestyle='--',linewidth =1,label='mean')
#one standard deviation
plt.axvline(mean+st_dev,color='green',linestyle='--',linewidth =1,label='±1 Std Dev')
plt.axvline(mean-st_dev,color='green',linestyle='--',linewidth =1)

#two standard deviation
plt.axvline(mean+(2*st_dev),color='blue',linestyle='--',linewidth =1,label='±2 Std Dev')
plt.axvline(mean-(2*st_dev),color='blue',linestyle='--',linewidth =1)#one standard deviation

#three standard deviation
plt.axvline(mean+(3*st_dev),color='red',linestyle='--',linewidth =1,label='±3 Std Dev')
plt.axvline(mean-(3*st_dev),color='red',linestyle='--',linewidth =1)
plt.legend()
plt.show()