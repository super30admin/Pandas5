import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, how='inner', left_on='departmentId', right_on='id')
    df['rnk'] = df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    df = df.sort_values(by='rnk', ascending=True)
    df = df[df['rnk'] == 1]
    df = df.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    return df[['Employee', 'Department', 'Salary']]
