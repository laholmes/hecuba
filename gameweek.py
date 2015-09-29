import nfldb
import json
import betting
from models.bet import Bet
import datetime

db = nfldb.connect()
q = nfldb.Query(db)

# print games for a given gameweek
def print_games(year, week):
    q.game(season_year=year, season_type='Regular', week=week)
    for g in q.as_games():
        print(g.gsis_id)
        print(g)

def calc_bets(data, week, threshold):
    bets = []
    q.game(season_year=2015, season_type='Regular', week=week)
    for g in q.as_games():
        betfairPriceHome = data['weeks'][week]['games'][g.gsis_id]['betfairPriceHome']
        betfairPriceAway = data['weeks'][week]['games'][g.gsis_id]['betfairPriceAway']
        homeTeamWeighting = data['weeks'][week]['games'][g.gsis_id]['homeTeamWeighting']
        awayTeamWeighting = data['weeks'][week]['games'][g.gsis_id]['awayTeamWeighting']

        betfairHomePercentage = 1.0 / (betfairPriceHome + 1)
        betfairAwayPercentage = 1.0 / (betfairPriceAway + 1)

        if(betfairHomePercentage + threshold <= homeTeamWeighting):
            bets.append({
                'team': 'home',
                'gameId': g.gsis_id,
                'netOdds': betfairPriceHome,
                'percentageWin': homeTeamWeighting
            })

        if(betfairAwayPercentage + threshold <= awayTeamWeighting):
            bets.append({
                'team': 'away',
                'gameId': g.gsis_id,
                'netOdds': betfairPriceAway,
                'percentageWin': awayTeamWeighting
            })
    return bets

def save_bets(bets, bankroll):
    for bet in bets:
        size = betting.kelly_size(bet['netOdds'], bet['percentageWin'], bankroll)
        proportion = betting.kelly_proportion(bet['netOdds'], bet['percentageWin'])

        Bet.insert(
            game_id = bet['gameId'],
            proportion = proportion,
            amount = size,
            date = datetime.datetime.now(),
            odds = bet['netOdds'],
            status = 0,
            account = 0
        )

        # for foo in Bet.select():
        #     print('from db!')
        #     print(foo.game_id)

# def get_bets(gameweek):
#     Bet.get(Bet.)


def get_bets():
    bets = Bet.get()
    return bets
