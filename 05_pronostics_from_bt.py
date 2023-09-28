import pandas as pd
from get_prob_util import ALL_POOL, pronostics, get_prob

df2 = pd.read_csv("bt/matrix_from_bradley_terry.csv", index_col=0)

print("** FROM BRADLEY-TERRY **")
for match in ALL_POOL:
    _, _ = pronostics(match, df2)
