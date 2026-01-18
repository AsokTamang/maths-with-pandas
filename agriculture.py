import pandas as pd
import openpyxl

df = pd.read_excel("C:/Users/ashok/Downloads/chapter4_exercise3/chapter4_exercise3/climate_stability_comparison.xlsx")
df.describe()
#calculate standard deviation for both City A and City B

# -----> 'City A' standard deviation
std_of_A=df['Avg Temp City A (°C)'].std()
print(std_of_A)

std_of_B=df['Avg Temp City B (°C)'].std()
print(std_of_B)

#variance of city B
print(df['Avg Temp City B (°C)'].var())

#variance of city A
print(df['Avg Temp City A (°C)'].var())

#as the variance as well as std of city A is much lesser compared to that of city B , which means the temperature of city B is much more volatile or less stable compared to that of city A across all 12 months,
#so its best to invest in agriculture firm at city A.

