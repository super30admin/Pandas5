import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # construct a rank column in prder by score descending 
    scores['rank'] = scores['score'].rank(method = 'dense', ascending= False)

    # order by rank in the result dataframe
    result_df = scores.sort_values(by = 'rank')

   
    return result_df[['score','rank']]