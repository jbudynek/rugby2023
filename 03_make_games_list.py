import json

import pandas as pd

PAGE_SIZE = 100

df = pd.DataFrame(columns=["date", "team_1", "team_2", "win_1", "win_2"])

idx = 0
invalid = 0
for year in range(2023, 2009, -1):
    with open(f"json/{year}-sample.json", "r") as infile:
        data = json.load(infile)

    num_entries = data["pageInfo"]["numEntries"]
    print(f"year {year} has {num_entries} entries")

    for page in range(0, num_entries // PAGE_SIZE + 1):
        print(f"getting year {year} page {page}")
        with open(f"json/{year}-{page:02}.json", "r") as infile:
            data = json.load(infile)
        for match in data["content"]:
            valid = True
            date = match["time"]["label"]
            team_1 = match["teams"][0]["abbreviation"]
            team_2 = match["teams"][1]["abbreviation"]
            win_1 = match["outcome"] == "A"
            win_2 = match["outcome"] == "B"
            if (
                (team_1 == None)
                or (team_2 == None)
                or (win_1 == False and win_2 == False)
            ):
                print(f"{date} {team_1} {team_2} {win_1} {win_2}")
                # print(match)
                valid = False
                invalid += 1
            if valid:
                df.loc[idx] = [date, team_1, team_2, win_1, win_2]
                idx += 1

    print(f"year {year} done")


df.sort_values("date", inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

print(f"{invalid} invalid matches")

df.to_csv("games/all_games.csv")


quit()
