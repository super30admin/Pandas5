import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the two dataframes
    combined_df = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'inner')

    # groupby departmentId by each unique Id and dense rank over desc
    combined_df['rnk'] = combined_df.groupby('departmentId')['salary'].rank(method = 'dense', ascending = False)

    #locate all the record series where rank=1
    result_df = combined_df.loc[combined_df['rnk']==1]


   
    return result_df[['name_y','name_x','salary']].rename(columns = {'name_y': 'Department','name_x':'Employee', 'salary':'Salary' })
     

    