import pandas as pd
import matplotlib.pyplot as plt
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


range_steps_taken = df.steps_taken.max() - df.steps_taken.min()
print(range_steps_taken)
# Calculate the range of "calories_burned" for the entire week
range_calories_burned = df.calories_burned.max() - df.calories_burned.min()
print(range_calories_burned)

# Calculate the Interquartile Range (IQR) for "sleep_duration(hours)"
qsd1,qsd2,qsd3 = df['sleep_duration(hours)'].quantile([0.25,0.5,0.75])
iqrsd = qsd3 - qsd1
print(iqrsd)



# Calculate the IQR for "water_intake(ounces)"
qw1,qw2,qw3 = df['water_intake(ounces)'].quantile([0.25,0.5,0.75])
iqrw = qw3 - qw1
print(iqrw)


#Box Plot for Steps Taken


# Set the figure size

plt.figure(figsize=(10,7))
df['steps_taken'].plot(kind='box',title = 'Steps_Taken Distribution', patch_artist=True)
plt.ylabel('Number of steps')
plt.tight_layout()
plt.show()



#Use the IQR method to identify and label outliers in the "sleep_duration(hours)" column.
lower_limit_sd = qsd1 - (1.5 * iqrsd)
print(lower_limit_sd)
upper_limit_sd = qsd3 + (1.5 * iqrsd)
print(upper_limit_sd)
outlier_sd =    df[(df['sleep_duration(hours)']<lower_limit_sd) | (df['sleep_duration(hours)']>upper_limit_sd)]
print(outlier_sd)