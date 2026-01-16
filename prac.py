#import necessary libraries
import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter4_exercise1/chapter4_exercise1/telecom_customer_churn.csv")
print(df.shape)
df.head(5)

#checking the datas
print(df.columns)
print(df.isnull())
print(df.info())   #checking the types and whether the column data is null or not
print(df.describe())

#converting the numeric column data types into same int type
#display all the column names
df['total_charges'] = pd.to_numeric(df.tenure)
df['monthly_charges'] = pd.to_numeric(df.tenure)
df['tenure'] = pd.to_numeric(df.tenure)
print(df.info())






