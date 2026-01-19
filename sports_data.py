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






mean_rate = df['player_rating'].mean()
std_rate= df.player_rating.std()

left1_rate = mean_rate-std_rate
right1_rate= mean_rate+std_rate
within_onerange_rate = df[(df.player_rating>left1) & (df.player_rating<right1)]


left2_rate = mean_rate- (2 * std_rate)
right2_rate = mean_rate+ (2*std_rate)
within_tworange_rate = df[(df.player_rating>left2) & (df.player_rating<right2)]

left3_rate = mean_rate- (3 * std_rate)
right3_rate = mean_rate+ (3 * std_rate)
within_threerange_rate = df[(df.player_rating>left3) & (df.player_rating<right3)]

sns.histplot(df['player_rating'],kde=True)
plt.axvline(x=mean_rate,color='black',linestyle='dashed',label='mean')
plt.axvline(x=left1_rate,color='g',linestyle='dashed',label='+-one std_age')
plt.axvline(x=right1_rate,color='g',linestyle='dashed')
plt.axvline(x=left2_rate,color='blue',linestyle='dashed',label='+-two std_age')
plt.axvline(x=right2_rate,color='blue',linestyle='dashed')
plt.axvline(x=left3_rate,color='red',linestyle='dashed',label='+-three std_age')
plt.axvline(x=right3_rate,color='red',linestyle='dashed')
plt.show()


lower_age_limit = mean_age - (3 * std_age)
upper_age_limit = mean_age + (3 * std_age)
lower_rate_limit = mean_rate - (3 * std_rate)
upper_rate_limit = mean_rate + (3 * std_rate)
outliers_age = df[(df['age']<lower_age_limit) | (df['age']>upper_age_limit)]
outliers_rate = df[(df['player_rating']<lower_rate_limit) | (df['player_rating']>upper_rate_limit)]

non_outliers= df[(df['age']>lower_age_limit) & (df['age']<upper_age_limit) & (df['player_rating']>lower_rate_limit) & (df['player_rating']<upper_rate_limit)]
plt.figure()
sns.histplot(non_outliers.age,kde=True)
plt.show()

plt.figure()
sns.histplot(non_outliers.player_rating,kde=True)
plt.show()


