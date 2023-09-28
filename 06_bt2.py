import pandas as pd
import numpy as np
import choix
from get_prob_util import get_prob

WORLD_CUP_TEAMS = [
    "ARG",
    "AUS",
    "CHI",
    "ENG",
    "FIJ",
    "FRA",
    "GEO",
    "IRE",
    "ITA",
    "JPN",
    "NAM",
    "NZL",
    "POR",
    "ROU",
    "RSA",
    "SAM",
    "SCO",
    "TGA",
    "URU",
    "WAL",
]

DBG = False
df = pd.read_csv("games/all_games.csv", index_col=0)
df.set_index("date", inplace=True)
print(df)

column1 = df["team_1"].values
column2 = df["team_2"].values

merged = np.concatenate((column1, column2))

unique_sorted = np.sort(np.unique(merged))

print(unique_sorted)

n_items = len(unique_sorted)

all_dates = df.index.values
all_dates = np.sort(all_dates)
print(all_dates[0], all_dates[-1])

start_y = 2010
end_y = 2023

while start_y <= end_y:
    start_date = str(start_y) + "-01-01"
    end_date = str(end_y) + "-12-31"

    mask = (df.index >= start_date) & (df.index <= end_date)
    filtered_df = df.loc[mask]
    print(filtered_df)

    data = []

    for t in filtered_df.itertuples():
        team_1 = t.team_1
        team_2 = t.team_2

        if team_1 in WORLD_CUP_TEAMS or team_2 in WORLD_CUP_TEAMS:
            win_1 = t.win_1
            win_2 = t.win_2
            idx1 = np.where(unique_sorted == team_1)
            idx2 = np.where(unique_sorted == team_2)
            if win_1:
                data.append((idx1, idx2))
            else:
                data.append((idx2, idx1))

    print(len(data))
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

    df2.to_csv(f"bt/matrix_from_bradley_terry_{start_y}.csv")
    start_y += 1

quit()
