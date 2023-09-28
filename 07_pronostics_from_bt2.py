import pandas as pd
import matplotlib.pyplot as plt
from get_prob_util import ALL_POOL, pronostics, get_prob

start_y0 = 2021
start_y = start_y0
end_y = 2023
whisk = {}
for match in ALL_POOL:
    whisk[tuple(match)] = []

while start_y <= end_y:
    df2 = pd.read_csv(f"br/matrix_from_bradley_terry_{start_y}.csv", index_col=0)

    print(f"** FROM BRADLEY-TERRY {start_y} **")
    for match in ALL_POOL:
        prob1, prob2 = pronostics(match, df2)
        whisk[tuple(match)].append(prob1)
    start_y += 1

for k, v in whisk.items():
    print(f"{k} {len(v)} {v}")


plt.ylim(0, 1)
plt.boxplot(whisk.values(), labels=whisk.keys())
plt.xticks(rotation=45)  #'vertical')
plt.title(f"Boxplots for rugby 2023 matches using data from {start_y0} to {end_y}")
plt.ylabel("Probability that team 1 wins")
plt.axhline(0.5, color="r", linestyle="--")
plt.tight_layout(pad=2.0)
plt.show()
fn = f"boxplots/whisk-{start_y0}-{end_y}.png"
plt.savefig(fn)
