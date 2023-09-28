import pandas as pd
from get_prob_util import ALL_POOL, pronostics, get_prob

df = pd.read_csv("ratings/matrix_from_ratings.csv", index_col=0)

print("** FROM RATINGS **")
for match in ALL_POOL:
    _, _ = pronostics(match, df)
