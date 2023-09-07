import json
import pandas as pd 
import numpy as np
import choix

DBG = False

with open('ratings-230907.json') as json_file:
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
	['FRA','NZL'],
#9/9
  	['ITA','NAM'],
	['IRE','ROU'],
	['AUS','GEO'],
	['ENG','ARG'],
#10/9  	
    ['RSA','SCO'],
	['WAL','FIJ'],
	['JPN','CHI'],
#14/9  	
    ['FRA','URU'],
#15/9  	
    ['NZL','NAM'],
#16/9  	
    ['IRE','TGA'],
	['WAL','POR'],
	['SAM','CHI'],
#17/9  	
    ['RSA','ROU'],
	['AUS','FIJ'],
	['ENG','JPN'],
#20/9  	
    ['ITA','URU'],
#21/9  	
    ['FRA','NAM'],
#22/9  	
    ['ARG','SAM'],
#23/9  	
    ['RSA','IRE'],
	['GEO','POR'],
	['ENG','CHI'],
#24/9  	
    ['SCO','TGA'],
	['WAL','AUS'],
#27/9  	
    ['URU','NAM'],
#28/9  	
    ['JPN','SAM'],
#29/9  	
    ['NZL','ITA'],
#30/9  	
    ['SCO','ROU'],
	['FIJ','GEO'],
	['ARG','CHI'],
#1/10  	['RSA','TGA'],
	['AUS','POR'],
#5/10  	
    ['NZL','URU'],
#6/10  	
    ['FRA','ITA'],
#7/10  	
    ['IRE','SCO'],
	['WAL','GEO'],
	['ENG','SAM'],
#8/10  	
    ['TGA','ROU'],
	['FIJ','POR'],
	['JPN','ARG'],
]


for match in all_pool:
    t1 = match[0]
    t2 = match[1]
    p1 = int(df2.at[t1,t2] * 1000)/10
    p2 = int(df2.at[t2,t1] * 1000)/10
    print(f"{t1} {p1}% -- {t2} {p2}%")

