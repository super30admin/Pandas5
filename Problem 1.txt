import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #First, we merge the employee and department dataframes 
    #using an inner join (default for merge)
    merged_df = employee.merge(department, left_on = 'departmentId', right_on = 'id')

    #Second, we rename the columns 
    #and take only the department, employee, and salary columns
    merged_df = merged_df.rename(columns = {'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]
    
    return merged_df[merged_df['Salary'] == merged_df.groupby('Department')['Salary'].transform(max)]