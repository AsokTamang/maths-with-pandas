import pandas as pd
import openpyxl
df = pd.read_excel("C:/Users/ashok/Downloads/chapter4_exercise2/chapter4_exercise2/fitness_data.xlsx")
df.head(5)
print(df['steps_taken'].mean())
