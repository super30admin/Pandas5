#Problem 1
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId',right_on='id',how='left')
    max_salary=df.groupby('departmentId')['salary'].transform('max')
    print(max_salary)
    df=df[df['salary']==max_salary]
    print(df)
    return df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee'})
    
#Problem 2
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']]
