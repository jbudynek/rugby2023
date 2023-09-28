import json
import pandas as pd
import numpy as np
from get_prob_util import get_prob

DBG = False

with open("ratings/ratings-230925.json") as json_file:
    data = json.load(json_file)

if DBG:
    print(data)

df = pd.DataFrame(data["entries"])

change_vals = lambda row: row.team["name"]

df["team_name"] = df.apply(change_vals, axis=1)

change_vals = lambda row: row.team["abbreviation"]
df["team_abbreviation"] = df.apply(change_vals, axis=1)

df = df.drop("team", axis=1)
df = df.drop("previousPts", axis=1)
df = df.drop("previousPos", axis=1)

params = df["pts"].to_numpy()
teams = df["team_abbreviation"].to_numpy()

# all to all

n = len(teams)
data = np.zeros(shape=(n, n))
index = teams
columns = teams
df2 = pd.DataFrame(data, index=index, columns=columns)

for t1 in teams:
    for t2 in teams:
        p = get_prob(t1, t2, teams, params)
        df2.at[t1, t2] = p

if DBG:
    print(df2)

df2.to_csv("ratings/matrix_from_ratings.csv")
quit()
