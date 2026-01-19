import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter6_assets/chapter6_assets/4_detect_outliers_using_normal_distribution/heights_with_outliers.csv")
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
#the datas beyond the three standard deviation are the outliers
plt.legend()
plt.show()  #before removing the outliers

left1 = mean-st_dev
right1=mean+st_dev

left2=mean-(2*st_dev)
right2=mean+(2*st_dev)

left3=mean-(3*st_dev)
right3=mean+(3*st_dev)

df_within_onerange = df[(df.height>left1) & (df.height<right1)].sort_values(by='height')  #retrieving the column of heights within the first standard deviation and sorting them by heights
print(df_within_onerange)

df_within_secondrange = df[(df.height>left2) & (df.height<right2)].sort_values(by='height')  #retrieving the column of heights within the first standard deviation and sorting them by heights
print(df_within_secondrange)

outliers = df[(df.height<left3) | (df.height>right3)]
print(outliers)

df= df[(df.height>left3) & (df.height<right3)]
sns.histplot(df)  #removing the outliers
plt.show()  #after removing the outliers





