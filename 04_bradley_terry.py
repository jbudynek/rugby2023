import choix
import numpy as np
import pandas as pd

from get_prob_util import WORLD_CUP_TEAMS, get_prob, BOUNDS

DBG = False

df = pd.read_csv("games/all_games.csv", parse_dates=["date"], index_col=0)
df.reset_index(drop=True)
df.set_index("date", inplace=True)

print(df)

all_team1 = df["team_1"].values
all_team2 = df["team_2"].values
merged = np.concatenate((all_team1, all_team2))
all_unique_teams = np.sort(np.unique(merged))

print(all_unique_teams)

n_items = len(all_unique_teams)

all_dates = df.index.values
all_dates = np.sort(all_dates)
print(all_dates[0], all_dates[-1])


start_y = 2010
end_y = 2023

for idx, val in enumerate(BOUNDS):
    if idx == 0:
        continue

    start_date = BOUNDS[idx - 1]
    end_date = BOUNDS[-1]

    mask = (df.index > start_date) & (df.index <= end_date)
    filtered_df = df[mask]
    print(filtered_df)

    data = []

    for t in filtered_df.itertuples():
        team_1 = t.team_1
        team_2 = t.team_2

        if team_1 in WORLD_CUP_TEAMS or team_2 in WORLD_CUP_TEAMS:
            win_1 = t.win_1
            win_2 = t.win_2
            idx1 = np.where(all_unique_teams == team_1)
            idx2 = np.where(all_unique_teams == team_2)
            if win_1:
                data.append((idx1, idx2))
            else:
                data.append((idx2, idx1))

    print(len(data))
    params = choix.ilsr_pairwise(n_items, data, alpha=0.01)
    # print(params)
    # print("ranking (worst to best):", np.argsort(params))
    print("ranking (worst to best):", all_unique_teams[np.argsort(params)])

    ###############################

    # all to all

    n = len(all_unique_teams)
    data = np.zeros(shape=(n, n))
    index = all_unique_teams
    columns = all_unique_teams
    df2 = pd.DataFrame(data, index=index, columns=columns)

    for t1 in all_unique_teams:
        for t2 in all_unique_teams:
            p = get_prob(t1, t2, all_unique_teams, params)
            df2.at[t1, t2] = p

    if DBG:
        print(df2)

    df2.to_csv(f"bt3/matrix_from_bradley_terry_{idx:02}.csv")
    start_y += 1

quit()
