import pandas as pd

df = pd.read_csv('matrix_from_ratings.csv',index_col=0)
df2 = pd.read_csv("matrix_from_bradley_terry.csv",index_col=0)

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
#    ["NZL", "URU"],
    # 6/10
#    ["FRA", "ITA"],
    # 7/10
#    ["WAL", "GEO"],
#    ["ENG", "SAM"],
#    ["IRE", "SCO"],
    # 8/10
#    ["JPN", "ARG"],
#    ["TGA", "ROU"],
#    ["FIJ", "POR"],
]


def pronostics(matrix):

    for match in ALL_POOL:
        t1 = match[0]
        t2 = match[1]
        p1 = int(matrix.at[t1, t2] * 1000) / 10
        p2 = int(matrix.at[t2, t1] * 1000) / 10
        print(f"{t1} {p1}% -- {t2} {p2}%")


print("** FROM RATINGS **")
pronostics(df)
print("** FROM BRADLEY-TERRY **")
pronostics(df2)

