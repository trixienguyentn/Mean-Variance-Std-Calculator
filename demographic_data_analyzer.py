import pandas as pd

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
           'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']

df = pd.read_csv(url, names=columns, na_values=" ?", skipinitialspace=True)

# How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()
print(race_counts)

# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(f"Average age of men: {average_age_men:.2f}")

# What is the percentage of people who have a Bachelor's degree?
bachelor_percentage = (df['education'] == 'Bachelors').mean() * 100
print(f"Percentage of people with a Bachelor's degree: {bachelor_percentage:.2f}%")

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
advanced_education_high_salary = (advanced_education['salary'] == '>50K').mean() * 100
print(f"Percentage of people with advanced education who make more than 50K: {advanced_education_high_salary:.2f}%")

# What percentage of people without advanced education make more than 50K?
no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

# Calculate the percentage of people without advanced education who earn >50K
no_advanced_education_high_salary = (no_advanced_education['salary'] == '>50K').mean() * 100
print(f"Percentage of people without advanced education who make more than 50K: {no_advanced_education_high_salary:.2f}%")

# What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()
print(f"Minimum number of hours worked per week: {min_hours_per_week}")

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
min_hours_high_salary_percentage = (min_hours_workers['salary'] == '>50K').mean() * 100
print(f"Percentage of people who work the minimum number of hours per week and earn more than 50K: {min_hours_high_salary_percentage:.2f}%")

# What country has the highest percentage of people that earn >50K and what is that percentage?
country_salary_percentage = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
highest_salary_country = country_salary_percentage.idxmax()
highest_salary_percentage = country_salary_percentage.max()
print(f"Country with the highest percentage of people earning >50K: {highest_salary_country}")
print(f"Percentage: {highest_salary_percentage:.2f}%")

# Identify the most popular occupation for those who earn >50K in India.
india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india = india_high_salary['occupation'].mode()[0]
print(f"Most popular occupation for people earning >50K in India: {most_popular_occupation_india}")