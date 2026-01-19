import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/ashok/Downloads/chapter6_exercise1/chapter6_exercise1/sports_league_data.csv")
print(df.shape)

#ranges of age

mean_age = df['age'].mean()
mean_age
std_age= df.age.std()
std_age


left1 = mean_age-std_age
right1= mean_age+std_age
within_onerange_age = df[(df.age>left1) & (df.age<right1)]


left2 = mean_age- (2 * std_age)
right2 = mean_age+ (2*std_age)
within_tworange_age = df[(df.age>left2) & (df.age<right2)]

left3 = mean_age- (3 * std_age)
right3 = mean_age+ (3 * std_age)
within_threerange_age = df[(df.age>left3) & (df.age<right3)]
print(within_onerange_age.shape)
print(within_tworange_age.shape)
print(within_threerange_age.shape)

sns.histplot(df['age'],kde=True)
plt.axvline(x=mean_age,color='black',linestyle='dashed',label='mean')
plt.axvline(x=left1,color='g',linestyle='dashed',label='+-one std_age')
plt.axvline(x=right1,color='g',linestyle='dashed')
plt.axvline(x=left2,color='blue',linestyle='dashed',label='+-two std_age')
plt.axvline(x=right2,color='blue',linestyle='dashed')
plt.axvline(x=left3,color='red',linestyle='dashed',label='+-three std_age')
plt.axvline(x=right3,color='red',linestyle='dashed')
plt.show()

