import nfldb
import json
from pprint import pprint
import betting
import datetime

DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'
db = nfldb.connect()
q = nfldb.Query(db)

threshold = 0.04
bets = []
bankroll = 100

def calcGameweekBets(week, threshold):
    q.game(season_year=2015, season_type='Regular', week=week)
    for g in q.as_games():
        betfairPriceHome = data["weeks"][week]["games"][g.gsis_id]["betfairPriceHome"]
        betfairPriceAway = data["weeks"][week]["games"][g.gsis_id]["betfairPriceAway"]
        homeTeamWeighting = data["weeks"][week]["games"][g.gsis_id]["homeTeamWeighting"]
        awayTeamWeighting = data["weeks"][week]["games"][g.gsis_id]["awayTeamWeighting"]

        betfairHomePercentage = 1.0 / (betfairPriceHome + 1)
        betfairAwayPercentage = 1.0 / (betfairPriceAway + 1)

        if(betfairHomePercentage + threshold <= homeTeamWeighting):
            bets.append({
                "team": "home",
                "gameId": g.gsis_id,
                "netOdds": betfairPriceHome,
                "percentageWin": homeTeamWeighting
            })

        if(betfairAwayPercentage + threshold <= awayTeamWeighting):
            bets.append({
                "team": "away",
                "gameId": g.gsis_id,
                "netOdds": betfairPriceAway,
                "percentageWin": awayTeamWeighting
            })
    return bets

def save_bets(bets):
    for bet in bets:
        # segment on week -> bankroll inc
        print(bet)
        size = betting.KellySize(bet.netOdds, bet.percentageWin, bankroll)

        Bet.create(
            game_id = bet["gameId"],
            amount = size,
            date = datetime.datetime.now(),
            odds = bet["netOdds"]
        )

with open("538.json") as data_file:
    data = json.load(data_file)

    for week in ["1","2"]:
        bets.append(calcGameweekBets(week, threshold))

    save_bets(bets)

# multiple trials for a given edge, assuming mean error = 0
# for the bets selected, generate random outcome set, 1000 times, show mean winning, std dev
# graph outcome
#profit = 0
#x = 0
#results = []
#while x < 1000:
#    for bet in bets:
#        outcome = random.randint(0,100)
#        bet["percentageWin"] #how often they winning
#        if(outcome <= bet["percentageWin"]):
#            #won the bet
#            profit += bet["size"]
#        else:
#            profit -= bet["size"]

#    print profit
#    results.append(profit)
#    x += 1

#import random

#sum results / 1000
#print('mean profit: ', )
#print('std dev of profit')
#use matplotlib to graph results
#def rollDice():
#	roll = random.randint(1, 100)


#placed bets
# gameweek 1: 100units
# panthers 11.6 units @ 1.625 status: Won
# cardinals 23.5 units @ 0.8 status: Won
# 49ers 35.1 units @ 1.1 status: Won
# = +(1.625*11.6)+(23.5*0.8)+(35.1*1.1) = +74 units 74% roi
# week 2: 174 units

# gameweek 2: 174 units


# run from cmd
if __name__ == '__main__':
    app.run()
