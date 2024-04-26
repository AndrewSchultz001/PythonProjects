import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

df = pd.read_csv("diabetes_binary_health_indicators_BRFSS2015.csv")

# Average age of people with diabetes
people_with_diab = df[df['Diabetes_binary'] == 1]

average_age_diabetes = people_with_diab['Age'].mean()

# Avgerage number of males with Diabetes
males = df[df['Sex'] == 1]
average_male_diabetes = males['Diabetes_binary'].mean()

# Avergae number of females with Diabetes
females = df[df['Sex'] ==0]
average_female_diabetes = females['Diabetes_binary'].mean()

# Avg number of people with HighBp with Diabetes
highbp = df[df['HighBP'] ==1]
average_highbp_diabetes = highbp['Diabetes_binary'].mean()

# Avg number of people with HighChol with Diabetes
highchol = df[df['HighChol'] ==1]
average_highchol_diabetes = highchol['Diabetes_binary'].mean()

# Avg number of people with HeartDieaseorAttack with Diabetes
heart = df[df['HeartDiseaseorAttack'] ==1]
average_heart_diabetes = heart['Diabetes_binary'].mean()

# Avg BMI of people with Diabetes
average_bmi_diabetes = people_with_diab['BMI'].mean()

# Avg number of people with HeartDieaseorAttack with Diabetes
fruit = df[df['Fruits'] ==1]
average_fruit_diabetes = fruit['Diabetes_binary'].mean()

'''
# Historgram of BMI vs #People with Diabetes
hist = df.hist('BMI', weights=df['Diabetes_binary'], bins=20) 
plt.xticks(np.arange(0, 100, step=5))
plt.xlabel("BMI")
plt.ylabel("Number of People with Diabetes")
plt.title("BMI to Number of People with Diabetes")
plt.savefig("BMIvsDiabtesHist.png")
plt.show()

# Histogram of Age vs #People with Diabetes
hist = df.hist('Age', weights=df['Diabetes_binary'], bins = 13)
plt.xticks(np.arange(0, 13, step=1))
plt.xlabel("Age Group")
plt.ylabel("Number of People with Diabetes")
plt.title("Age to Number of People with Diabetes")
plt.savefig("AgevsDiabetesHist")
plt.show()
'''

# Linear Regression Model between BMI and Number of People with Diabetes
result = scipy.stats.linregress(df['HighBP'], df['Diabetes_binary'])
print("HighBP")
print(result.rvalue)

result = scipy.stats.linregress(df['HighChol'], df['Diabetes_binary'])
print("HighChol")
print(result.rvalue)

result = scipy.stats.linregress(df['HeartDiseaseorAttack'], df['Diabetes_binary'])
print("HeartDiseaseorAttack")
print(result.rvalue)

result = scipy.stats.linregress(df['Age'], df['Diabetes_binary'])
print("Age")
print(result.rvalue)

result = scipy.stats.linregress(df['BMI'], df['Diabetes_binary'])
print("BMI")
print(result.rvalue)

result = scipy.stats.linregress(df['DiffWalk'], df['Diabetes_binary'])
print("DiffWalk")
print(result.rvalue)

result = scipy.stats.linregress(df['PhysHlth'], df['Diabetes_binary'])
print("PhysHlth")
print(result.rvalue)

result = scipy.stats.linregress(df['GenHlth'], df['Diabetes_binary'])
print("GenHlth")
print(result.rvalue)
print(result.slope)
print(result.intercept)

#GenHlth
x_scatter_values = [1, 2, 3, 4, 5]
y_scatter_values = []
for i in range(1, 6):
    GenHlth = df[df['GenHlth'] == i]
    y_scatter_values.append(GenHlth['Diabetes_binary'].mean())

result = scipy.stats.linregress(x_scatter_values, y_scatter_values)
print("GenHlth2")
print(result.rvalue)
print(result.slope)

x_values = np.linspace(0, 5, 10)  
y_values = result.slope * x_values + result.intercept

plt.plot(x_values, y_values, label='Line')
plt.scatter(x_scatter_values, y_scatter_values, color='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.legend()
plt.show()

#Age
x_scatter_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y_scatter_values = []
for i in range(1, 14):
    age = df[df['Age'] == i]
    y_scatter_values.append(age['Diabetes_binary'].mean())

result = scipy.stats.linregress(x_scatter_values, y_scatter_values)
print("Age")
print(result.rvalue)
print(result.slope)

x_values = np.linspace(0, 13, 20)  
y_values = result.slope * x_values + result.intercept

plt.plot(x_values, y_values, label='Line')
plt.scatter(x_scatter_values, y_scatter_values, color='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.legend()
plt.show()

#BMI
x_scatter_values = df['BMI'].unique()
y_scatter_values = []
for i in range(0, len(x_scatter_values)):
    age = df[df['BMI'] == x_scatter_values[i]]
    y_scatter_values.append(age['Diabetes_binary'].mean())

result = scipy.stats.linregress(x_scatter_values, y_scatter_values)
print("BMI2")
print(result.rvalue)
print(result.slope)

x_values = np.linspace(0, 100, 100)  
y_values = result.slope * x_values + result.intercept

plt.plot(x_values, y_values, label='Line')
plt.scatter(x_scatter_values, y_scatter_values, color='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.legend()
plt.show()