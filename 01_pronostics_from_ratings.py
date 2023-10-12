import pandas as pd

from get_prob_util import ALL_FINAL_ROUNDS, pronostics

df = pd.read_csv("ratings/matrix_from_ratings.csv", index_col=0)

print("** FROM RATINGS **")
for match in ALL_FINAL_ROUNDS:
    _, _ = pronostics(match, df)
