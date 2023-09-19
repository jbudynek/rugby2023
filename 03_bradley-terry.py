import pandas as pd
import numpy as np
import choix
from get_prob_util import get_prob

DBG = False
df = pd.read_csv("all_games.csv", index_col=0)

print(df)

column1 = df["team_1"].values
column2 = df["team_2"].values

merged = np.concatenate((column1, column2))

unique_sorted = np.sort(np.unique(merged))

print(unique_sorted)

n_items = len(unique_sorted)
data = []

for t in df.itertuples():
    team_1 = t.team_1
    team_2 = t.team_2
    win_1 = t.win_1
    win_2 = t.win_2
    idx1 = np.where(unique_sorted == team_1)
    idx2 = np.where(unique_sorted == team_2)
    if win_1:
        data.append((idx1, idx2))
    else:
        data.append((idx2, idx1))

params = choix.ilsr_pairwise(n_items, data, alpha=0.01)
# print(params)
# print("ranking (worst to best):", np.argsort(params))
print("ranking (worst to best):", unique_sorted[np.argsort(params)])

###############################

# all to all

n = len(unique_sorted)
data = np.zeros(shape=(n, n))
index = unique_sorted
columns = unique_sorted
df2 = pd.DataFrame(data, index=index, columns=columns)

for t1 in unique_sorted:
    for t2 in unique_sorted:
        p = get_prob(t1, t2, unique_sorted, params)
        df2.at[t1, t2] = p

if DBG:
    print(df2)

df2.to_csv("matrix_from_bradley_terry.csv")

quit()

# POOL GAMES
all_pool = [
    # POOL 1
    # 	['FRA','NZL'],
    # 9/9
    #  	['ITA','NAM'],
    # 	['IRE','ROU'],
    # 	['AUS','GEO'],
    # 	['ENG','ARG'],
    # 10/9
    #   ['RSA','SCO'],
    # 	['WAL','FIJ'],
    # 	['JPN','CHI'],
    # POOL 2 - 14/9
    #   ['FRA','URU'],
    # 15/9
    #   ['NZL','NAM'],
    # 16/9
    # 	['SAM','CHI'],
    # 	['WAL','POR'],
    #   ['IRE','TGA'],
    # 17/9
    #   ['RSA','ROU'],
    # 	['AUS','FIJ'],
    # 	['ENG','JPN'],
    # POOL 3 - 20/9
    ["ITA", "URU"],
    # 21/9
    ["FRA", "NAM"],
    # 22/9
    ["ARG", "SAM"],
    # 23/9
    ["GEO", "POR"],
    ["ENG", "CHI"],
    ["RSA", "IRE"],
    # 24/9
    ["SCO", "TGA"],
    ["WAL", "AUS"],
    # POOL 4 - 27/9
    ["URU", "NAM"],
    # 28/9
    ["JPN", "SAM"],
    # 29/9
    ["NZL", "ITA"],
    # 30/9
    ["ARG", "CHI"],
    ["FIJ", "GEO"],
    ["SCO", "ROU"],
    # 1/10
    ["AUS", "POR"],
    ["RSA", "TGA"],
    # POOL 5 - 5/10
    ["NZL", "URU"],
    # 6/10
    ["FRA", "ITA"],
    # 7/10
    ["WAL", "GEO"],
    ["ENG", "SAM"],
    ["IRE", "SCO"],
    # 8/10
    ["JPN", "ARG"],
    ["TGA", "ROU"],
    ["FIJ", "POR"],
]


for match in all_pool:
    t1 = match[0]
    t2 = match[1]
    p1 = int(df2.at[t1, t2] * 1000) / 10
    p2 = int(df2.at[t2, t1] * 1000) / 10
    print(f"{t1} {p1}% -- {t2} {p2}%")
