import pandas as pd

# Step 0: Create the employee dataframe
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]
}
employee_df = pd.DataFrame(data)

# 1. Use iloc to select the first 3 rows of the dataframe
first_3_rows = employee_df.iloc[:3]
print("1. First 3 rows:\n", first_3_rows, "\n")

# 2. Use loc to select all rows where the Department is "Marketing"
marketing_employees = employee_df.loc[employee_df['Department'] == 'Marketing']
print("2. Employees in Marketing:\n", marketing_employees, "\n")

# 3. Use iloc to select Age and Gender columns for the first 4 rows
# Age = column index 2, Gender = column index 3
age_gender_first_4 = employee_df.iloc[:4, [2, 3]]
print("3. Age and Gender (first 4 rows):\n", age_gender_first_4, "\n")

# 4. Use loc to select Salary and Experience columns for rows where Gender is "Male"
salary_experience_males = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]
print("4. Salary and Experience (Males):\n", salary_experience_males)
