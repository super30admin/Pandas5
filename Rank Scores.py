import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method='dense', ascending=False)
    df = scores[["score", "rank"]].sort_values(by="rank")
    return df