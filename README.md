# hecuba
A football analysis tool written in python

TODO
- take 538 predictions and input into SQLite DB (python + peewee)
- key matches to game week
- script to pull games matching edge threshold (configurable e.g. 3% on betfair)
- matching games bet size selection based on kelly criterion
- simulate 1000 times w/100 unit portfolio, weighting according to kelly
- analyse std dev and variance
- then try other weightings - monte carlo to find optimal
- try adjusting threshold, look at impact on risk-adjusted return
- find optimal threshold w/monte carlo
- mean is predicted win
- place bets and record outcome
- scraper for 538
