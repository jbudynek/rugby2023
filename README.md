# Rugby 2023

## 230907 - One day to go

OK I'm super late since it starts tomorrow!

Links I found useful:
- Official rankings, but hard to use as is: https://www.world.rugby/tournaments/rankings/mru
- API to get the rankings in json form: https://api.wr-rims-prod.pulselive.com/rugby/v3/rankings/mru
- Sourced from https://github.com/rawling/wr-calc/ and https://rawling.github.io/wr-calc/


Got the World Rankings and points in json, parsed them, then used `choix` to generate probabilities of win for all possible games. I used this tutorial: https://github.com/lucasmaystre/choix/blob/master/notebooks/intro-pairwise.ipynb

Then, simply print probabilities as % for the pool games.
GPT sped me up a lot, I used it as a coding assistant.

Next, I would like to see whether the points ranking from the Rugby world site is really a good input for `choix`, and get some kind of confidence interval. Additionally I could generate my own parameters based on past games, that would be more in the Bradlet-Terry spirit.

By the way, here are the predictions: 

<details>
 <summary>Pool games!</summary>
 
```
FRA 54.1% -- NZL 45.8%
ITA 99.9% -- NAM 0.0%
IRE 99.9% -- ROU 0.0%
AUS 97.4% -- GEO 2.5%
ENG 28.6% -- ARG 71.3%
RSA 99.9% -- SCO 0.0%
WAL 11.6% -- FIJ 88.3%
JPN 99.9% -- CHI 0.0%
FRA 99.9% -- URU 0.0%
NZL 99.9% -- NAM 0.0%
IRE 99.9% -- TGA 0.0%
WAL 99.9% -- POR 0.0%
SAM 99.9% -- CHI 0.0%
RSA 99.9% -- ROU 0.0%
AUS 39.8% -- FIJ 60.1%
ENG 99.8% -- JPN 0.1%
ITA 99.9% -- URU 0.0%
FRA 99.9% -- NAM 0.0%
ARG 99.0% -- SAM 0.9%
RSA 32.2% -- IRE 67.7%
GEO 99.9% -- POR 0.0%
ENG 99.9% -- CHI 0.0%
SCO 99.9% -- TGA 0.0%
WAL 16.6% -- AUS 83.3%
URU 99.3% -- NAM 0.6%
JPN 5.2% -- SAM 94.7%
NZL 99.9% -- ITA 0.0%
SCO 99.9% -- ROU 0.0%
FIJ 98.2% -- GEO 1.7%
ARG 99.9% -- CHI 0.0%
AUS 99.9% -- POR 0.0%
NZL 99.9% -- URU 0.0%
FRA 99.9% -- ITA 0.0%
IRE 99.9% -- SCO 0.0%
WAL 88.3% -- GEO 11.6%
ENG 97.7% -- SAM 2.2%
TGA 99.6% -- ROU 0.3%
FIJ 99.9% -- POR 0.0%
JPN 0.0% -- ARG 99.9%
```

</details>

## 230831 - Introduction

The Rugby World cup is about to start, and I have been invited to a pronostic league by my colleagues.
I have been using random Excel formulas for years to predict outcomes in the Football world cups, with limited success.
This time I want to explore how to generate sensible pronostics in a data-driven fashion. This is my journal. Yay!

So, first thing, I remembered my ex-colleague Dr. Fabien Llobell explained how to predict winners for the football world cup in 2022.
He is head of research at the company that sells a widely used statistics plugin for Excel (disclaimer: I used to work there too), so for sure he knows what he's talking about. Here is his write-up: https://medium.com/xlstat/football-score-predictions-with-the-bradley-terry-model-e0a8a7ebfd83

So, the take-away is: use the Bradley-Terry model. Fine. I want to understand what this model does, how it works. I want to generate a probability of winning the next game for arbitrary teams, with confidence level. And I want to do it in Python.

Here are a few pointers that seem of interest.

- Mandatory Wikipedia link: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
- Of course R has a sophisticated implementation. Reading this page will help: https://www.r-bloggers.com/2022/02/what-is-the-bradley-terry-model/
- This guy has Jupyter notebooks that seem to do just what I want. This should be useful: https://github.com/sezenack/Bradley-Terry-Sports-Model
- `choix` is a Python lib that has a Bradley-Terry implementation, with tutorials. High hopes for this: https://github.com/lucasmaystre/choix

OK that should be good starting points. Of course, I also want to use GPT to help me out. Let's see how this goes.
