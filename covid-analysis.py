import pandas as pd

# Load the dataset from a local CSV file
file_path = r"C:\Users\Administrator\Python312\Scripts\Covid Analysis.csv"
df = pd.read_csv(file_path)

# Task 1: Find the Number of Unique Countries
num_unique_countries = df['Country/Region'].nunique()
print(f"Task 1 - Number of Unique Countries: There are {num_unique_countries} unique countries in
the dataset.\n")

# Task 2: Check the Null values in the Dataset
null_values = df.isnull().sum()
print("Task 2 - Null Values in the Dataset:")
print(null_values)
print()

# Task 3: Which Country has the maximum number of confirmed cases
max_confirmed_country = df.loc[df['Confirmed'].idxmax()]['Country/Region']
max_confirmed_cases = df['Confirmed'].max()
print(f"Task 3 - Country with the maximum number of confirmed cases: {max_confirmed_country}
has the highest number of confirmed cases with {max_confirmed_cases} cases.\n")

# Task 4: Which Country has the maximum number of deaths
max_deaths_country = df.loc[df['Deaths'].idxmax()]['Country/Region']
max_deaths = df['Deaths'].max()
print(f"Task 4 - Country with the maximum number of deaths: {max_deaths_country} has the highest
number of deaths with {max_deaths} deaths.\n")

# Task 5: What is the average number of cases across all countries
average_confirmed_cases = df['Confirmed'].mean()
print(f"Task 5 - Average number of confirmed cases across all countries: The average number of
confirmed cases is {average_confirmed_cases}.\n")

# Task 6: What is the total number of deaths as per the dataset
total_deaths = df['Deaths'].sum()
print(f"Task 6 - Total number of deaths as per the dataset: The dataset records a total of {total_deaths}
deaths.\n")

# Task 7: What is the total number of confirmed cases
total_confirmed_cases = df['Confirmed'].sum()
print(f"Task 7 - Total number of confirmed cases as per the dataset: The dataset records a total of
{total_confirmed_cases} confirmed cases.\n")

# Task 8: Which country has the highest death percentage
max_death_percentage_country = df.loc[df['Deaths / 100 Cases'].idxmax()]['Country/Region']
max_death_percentage = df['Deaths / 100 Cases'].max()
print(f"Task 8 - Country with the highest death percentage: {max_death_percentage_country} has the
highest death percentage with {max_death_percentage}%.\n")

# Task 9: Which country has the highest recovery percentage
max_recovery_percentage_country = df.loc[df['Recovered / 100 Cases'].idxmax()]['Country/Region']
max_recovery_percentage = df['Recovered / 100 Cases'].max()
print(f"Task 9 - Country with the highest recovery percentage: {max_recovery_percentage_country}
has the highest recovery percentage with {max_recovery_percentage}%.\n")

# Task 10: Create a New Column - New Cases to Active Cases Ratio
df['New Cases to Active Cases Ratio'] = df['New cases'] / df['Active']
print("Task 10 - New Column Added: 'New Cases to Active Cases Ratio'\n")

# Task 11: Create a New DataFrame for the Africa WHO Region
africa_df = df[df['WHO Region'] == 'Africa']
print("Task 11 - New Data Frame for Africa WHO Region Created\n")