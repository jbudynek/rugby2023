import json
import pandas as pd 
import numpy as np
import choix

DBG = False

with open('ratings-230918.json') as json_file:
    data = json.load(json_file)

if DBG: print(data)

df = pd.DataFrame(data['entries'])

change_vals = lambda row: row.team['name']

df['team_name'] = df.apply(change_vals, axis=1)

change_vals = lambda row: row.team['abbreviation']
df['team_abbreviation'] = df.apply(change_vals, axis=1)

df = df.drop('team',axis=1)
df = df.drop('previousPts',axis=1)
df = df.drop('previousPos',axis=1)

params = df['pts'].to_numpy()
teams = df['team_abbreviation'].to_numpy()

def get_prob(t1,t2):

    idx1 = np.where(teams==t1)[0][0]
    idx2 = np.where(teams==t2)[0][0]

    if DBG:
        print(t1,idx1,teams[idx1],params[idx1])
        print(t2,idx2,teams[idx2],params[idx2])

    prob_1_wins, prob_2_wins = choix.probabilities([idx1, idx2], params)
    if DBG:
        print(f"Prob({t1} wins over {t2}): {prob_1_wins:.2f}")
        print(f"Prob({t2} wins over {t1}): {prob_2_wins:.2f}")

    return prob_1_wins

# all to all

n = len(teams)
data = np.zeros(shape=(n, n))
index = teams
columns = teams
df2 = pd.DataFrame(data, index=index, columns=columns)

for t1 in teams:
    for t2 in teams:
        p = get_prob(t1,t2)
        df2.at[t1,t2] = p

if DBG: print(df2)

# POOL GAMES
all_pool = [
#POOL 1
#	['FRA','NZL'],
#9/9
#  	['ITA','NAM'],
#	['IRE','ROU'],
#	['AUS','GEO'],
#	['ENG','ARG'],
#10/9  	
#   ['RSA','SCO'],
#	['WAL','FIJ'],
#	['JPN','CHI'],
#POOL 2 - 14/9  	
#   ['FRA','URU'],
#15/9  	
#   ['NZL','NAM'],
#16/9  	
#	['SAM','CHI'],
#	['WAL','POR'],
#   ['IRE','TGA'],
#17/9  	
#   ['RSA','ROU'],
#	['AUS','FIJ'],
#	['ENG','JPN'],
#POOL 3 - 20/9  	
    ['ITA','URU'],
#21/9  	
    ['FRA','NAM'],
#22/9  	
    ['ARG','SAM'],
#23/9  	
	['GEO','POR'],
	['ENG','CHI'],
    ['RSA','IRE'],
#24/9  	
    ['SCO','TGA'],
	['WAL','AUS'],
# POOL 4 - 27/9  	
    ['URU','NAM'],
#28/9  	
    ['JPN','SAM'],
#29/9  	
    ['NZL','ITA'],
#30/9  	
	['ARG','CHI'],
	['FIJ','GEO'],
    ['SCO','ROU'],
#1/10
	['AUS','POR'],
  	['RSA','TGA'],
# POOL 5 - 5/10  	
    ['NZL','URU'],
#6/10  	
    ['FRA','ITA'],
#7/10  	
	['WAL','GEO'],
	['ENG','SAM'],
    ['IRE','SCO'],
#8/10  	
	['JPN','ARG'],
    ['TGA','ROU'],
	['FIJ','POR'],
]


for match in all_pool:
    t1 = match[0]
    t2 = match[1]
    p1 = int(df2.at[t1,t2] * 1000)/10
    p2 = int(df2.at[t2,t1] * 1000)/10
    print(f"{t1} {p1}% -- {t2} {p2}%")

