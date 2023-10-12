import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from get_prob_util import ALL_FINAL_ROUNDS, pronostics, BOUNDS

whisk = {}
for match in ALL_FINAL_ROUNDS:
    whisk[tuple(match)] = []

for idx, val in enumerate(BOUNDS):
    if idx == 0:
        continue

    start_date = BOUNDS[idx - 1]
    end_date = BOUNDS[-1]

    df2 = pd.read_csv(f"bt3/matrix_from_bradley_terry_{idx:02}.csv", index_col=0)

    print(f"** Using data from {start_date} to {end_date} **")
    for match in ALL_FINAL_ROUNDS:
        prob1, prob2 = pronostics(match, df2)
        whisk[tuple(match)].append(prob1)

print(f"** Game - list of prob - average prob - med prob **")
for k, v in whisk.items():
    formatted_data = ', '.join([f'{value:.2f}' for value in v])
    av = np.average(v)
    me = np.median(v)
    print(f"{k} [{formatted_data}] {av:.2f} {me:.2f}")


plt.ylim(0, 1)
plt.boxplot(whisk.values(), labels=whisk.keys())
plt.xticks(rotation=45)
plt.title(
    f"Boxplots for rugby 2023 quarters\nusing data from {BOUNDS[0]} to {BOUNDS[-1]}"
)
plt.ylabel("Probability that team 1 wins")
plt.axhline(0.5, color="r", linestyle="--")
plt.tight_layout(pad=2.0)
plt.show()
fn = f"boxplots/whisk-{BOUNDS[0]}-{BOUNDS[-1]}.png"
plt.savefig(fn)
