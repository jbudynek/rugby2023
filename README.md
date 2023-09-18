# Rugby 2023

## 230918 Pool #3 games

Here they are, done with the latest ratings. Three games look undecided.

<details>
 <summary>Pool #3 games!</summary>

```
ITA 99.9% -- URU 0.0%
FRA 99.9% -- NAM 0.0%
ARG 80.1% -- SAM 19.8%
GEO 99.6% -- POR 0.3%
ENG 99.9% -- CHI 0.0%
RSA 46.1% -- IRE 53.8%
SCO 99.9% -- TGA 0.0%
WAL 84.0% -- AUS 15.9%
```

</details>

## 230918 - Results pool 2
So, how did it go with the second  phase? Well I got 87.5% of winners right (7 out 8). Admittedly this round 2 was not surprising except for FIJ which seems to be a real outlier performer! All in all I got 13 out of 16, so 81.25% right so far.

<details>
 <summary>Results of second round of pool games</summary>

My bets are in bold.

| Team 1 | Team 2 | Winner | 1 if the bet is right |
|--|--|--|--|
|**FRA** |URU| **FRA**|1|
|**NZL** |NAM |**NZL**|1|
|**SAM** |CHI |**SAM**|1|
|**WAL** |POR |**WAL**|1|
|**IRE** |TGA |**IRE**|1|
|**RSA** |ROU |**RSA**|1|
|**AUS** |FIJ |**FIJ**|0|
|**ENG** |JPN |**ENG**|1|

</details>

## 230912 - bets on pool #2

Here they are, done with the latest ratings. Seems all straightforward, but who knows what will happen?

<details>
 <summary>Pool #2 games!</summary>
 
```
FRA 99.9% -- URU 0.0%
NZL 99.9% -- NAM 0.0%
SAM 99.9% -- CHI 0.0%
WAL 99.9% -- POR 0.0%
IRE 99.9% -- TGA 0.0%
RSA 99.9% -- ROU 0.0%
AUS 98.0% -- FIJ 1.9%
ENG 99.9% -- JPN 0.0%
```

</details>

Notes to self: What I would like to do - get some sort of confidence interval. Maybe use historical data to compute my own ranking, using Bradley-Terry, which is what I wanted to do initially. By using more or less historical data, I could make several models, and get a confidence interval like that.

## 230912 - After first phase of pool games
So, how did it go with the first phase? Well I got 75% of winners right (6 out 8)

<details>
 <summary>Results of first round of pool games</summary>

My bets are in bold.

| Team 1 | Team 2 | Winner | 1 if the bet is right |
|--|--|--|--|
|**FRA** |NZL| **FRA**|1|
|**ITA** |NAM |**ITA**|1|
|**IRE** |ROU |**IRE**|1|
|**AUS** |GEO |**AUS**|1|
|ENG |**ARG** |**ENG**|0|
|**RSA** |SCO |**RSA**|1|
|WAL |**FIJ** |**WAL**|0|
|**JPN** |CHI |**JPN**|1|

</details>

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
