import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter6_assets/chapter6_assets/3_normal_distribution/heights.csv")
sns.histplot(df,kde=True)
plt.show()