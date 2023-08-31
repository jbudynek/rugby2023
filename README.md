# rugby2023


## 230831 - Introduction

The Rugby World cup is about to start, and I have been invited to a pronostic league by my colleagues.
I have been using random Excel formulas for years to predict outcomes in the Football world cups, with limited success.
This time I want to explore how to generate sensible pronostics in a data-driven fashion. This is my journal. Yay!

So, first thing, I remembered my ex-colleague Dr. Fabien Lobell explained how to predict winners for the football world cup in 2022.
He is head of research at the company that sells a widely used statistics plugin for Excel (disclaimer: I used to work there too), so for sure he knows what he's talking about. Here is his write-up: https://medium.com/xlstat/football-score-predictions-with-the-bradley-terry-model-e0a8a7ebfd83

So, the take-away is: use the Bradley-Terry model. Fine. I want to understand what this model does, how it works. I want to generate a probability of winning the next game for arbitrary teams, with confidence level. And I want to do it in Python.

Here are a few pointers that seem of interest.

https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
Mandatory Wikipedia link.

https://www.r-bloggers.com/2022/02/what-is-the-bradley-terry-model/
Of course R has a sophisticated implementation. Reading this page will help.

https://github.com/sezenack/Bradley-Terry-Sports-Model
This guy has Jupyter notebooks that seem to do just what I want. This should be useful.

https://github.com/lucasmaystre/choix
Choix is a Python lib that has a Bradley-Terry implementation, with tutorials. High hopes for this.

OK that should be good starting points. Of course, I also want to use GPT to help me out. Let's see how this goes.
