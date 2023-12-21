#Question1 :

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department , left_on = 'departmentId' , right_on = 'id', how = 'left')
    top_sal = df.groupby('departmentId')['salary'].transform(max)
    df = df[df['salary'] == top_sal]
    return df[['name_y','name_x','salary']].rename(columns = {'name_y' :'Department' , 'name_x' : 'Employee','salary' : 'Salary'})

#Question2 : 
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method = 'dense' , ascending = False)
    return scores[['score' , 'rank']].sort_values(by = 'score',ascending = False)