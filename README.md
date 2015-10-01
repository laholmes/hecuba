# hecuba
A football analysis tool written in python

hecuba uses predictions from 538.com, and compares them against required breakeven win %s based on betfair prices pre-game.

Where profitable opportunities exist (i.e. win rate higher than required breakeven rate + threshold), hecuba computes optimal bet-size according to kelly criterion, and returns a list of bets to make.

hecuba uses nfldb/nflgame (postgres) for underlying db of players/games/teams, augmenting with prediction stats from 538.

hecuba saves bets to a sqlite db, using pewee ORM.

TODO
- simulate game runs 1000 times (based on 538 predictions) w/100 unit portfolio, weighting according to kelly + analyse
- then try other weightings - monte carlo to find optimal
- try adjusting threshold, look at impact on risk-adjusted return
- place bets and record outcome
- scraper for 538
- extract interaction with nfldb to service
