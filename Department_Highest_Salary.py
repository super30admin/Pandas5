import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #result = []
    employee = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'inner')
    employee['rank'] = employee.groupby(['departmentId'])['salary'].rank(method = 'dense',
                                                                    ascending = False)
    employee = employee[employee['rank'] == 1]
    return employee[['name_y', 'name_x', 'salary']].rename(columns = {'name_y':'Department',
    'name_x':'Employee'})