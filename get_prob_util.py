import choix
import numpy as np

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

BOUNDS = [
    #"2018-12-31",
    #"2019-06-30",
    "2019-12-31",
    "2020-06-30",
    "2020-12-31",
    "2021-06-30",
    "2021-12-31",
    "2022-05-30",
    "2022-12-31",
    "2023-06-30",
    "2023-12-31",
]

# FINALS
ALL_FINAL_ROUNDS = [
    # QUARTERS
    # 14/10
#      	['WAL','ARG'],
#     	['IRE','NZL'],
    # 15/10
#     	['ENG','FIJ'],
#     	['FRA','RSA'],
    # SEMIS
    # 20/10
#       ['ARG','NZL'],
    # 21/10
#     	['ENG','RSA'],
    # FINALS
    # 27/10
     	['ARG','ENG'],
    # 28/10
     	['NZL','RSA'],
]

# POOL GAMES
ALL_POOL = [
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
    #    ["ITA", "URU"],
    # 21/9
    #    ["FRA", "NAM"],
    # 22/9
    #    ["ARG", "SAM"],
    # 23/9
    #    ["GEO", "POR"],
    #    ["ENG", "CHI"],
    #    ["RSA", "IRE"],
    # 24/9
    #    ["SCO", "TGA"],
    #    ["WAL", "AUS"],
    # POOL 4 - 27/9
    #    ["URU", "NAM"],
    # 28/9
    #    ["JPN", "SAM"],
    # 29/9
    #    ["NZL", "ITA"],
    # 30/9
    #    ["ARG", "CHI"],
    #    ["FIJ", "GEO"],
    #    ["SCO", "ROU"],
    # 1/10
    #    ["AUS", "POR"],
    #    ["RSA", "TGA"],
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




def pronostics(match, matrix):
    t1 = match[0]
    t2 = match[1]
    prob1 = matrix.at[t1, t2]
    prob2 = matrix.at[t2, t1]
    p1 = int(prob1 * 1000) / 10
    p2 = int(prob2 * 1000) / 10
    print(f"{t1} {p1}% -- {t2} {p2}%")
    return (prob1, prob2)


def get_prob(t1, t2, teams, params, DBG=False):
    idx1 = np.where(teams == t1)[0][0]
    idx2 = np.where(teams == t2)[0][0]

    if DBG:
        print(t1, idx1, teams[idx1], params[idx1])
        print(t2, idx2, teams[idx2], params[idx2])

    prob_1_wins, prob_2_wins = choix.probabilities([idx1, idx2], params)
    if DBG:
        print(f"Prob({t1} wins over {t2}): {prob_1_wins:.2f}")
        print(f"Prob({t2} wins over {t1}): {prob_2_wins:.2f}")

    return prob_1_wins
