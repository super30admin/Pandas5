import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method = 'dense',ascending=False).astype(int)
    df = employee[employee['rank'] == 1][['departmentId','name','salary']].merge(department,how='left',left_on='departmentId',right_on='id')
    return df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})