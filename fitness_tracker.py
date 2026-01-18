import pandas as pd
import openpyxl
#You work for a fitness company and have gathered data on the fitness activities of 50 individuals using fitness trackers. The dataset is stored in an Excel file named "fitness_data.xlsx" and includes the following columns:
#name: Name of the person.
#steps_taken: The number of steps taken by individuals.
#calories_burned: The estimated calories burned by individuals.
#sleep_duration(hours): The number of hours of sleep individuals got on that day.
#water_intake(ounces): The amount of water individuals consumed.

df = pd.read_excel("C:/Users/ashok/Downloads/chapter4_exercise2/chapter4_exercise2/fitness_data.xlsx")
df.head(5)
print(df['steps_taken'].mean())  #mean of steps taken
print(df['calories_burned'].mean())  #mean of calories burned
print(df.describe())   #getting the statistical datas on every numerical columns
