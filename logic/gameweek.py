import nfldb
import json
import utilities.math_utilities as math_utilities
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
                'percentageWin': homeTeamWeighting,
                'gameweek': week
            })

        if(betfairAwayPercentage + threshold <= awayTeamWeighting):
            bets.append({
                'team': 'away',
                'gameId': g.gsis_id,
                'netOdds': betfairPriceAway,
                'percentageWin': awayTeamWeighting,
                'gameweek': week
            })
    return bets

def save_bets(bets, bankroll):
    for bet in bets:
        size = math_utilities.kelly_size(bet['netOdds'], bet['percentageWin'], bankroll)
        proportion = math_utilities.kelly_proportion(bet['netOdds'], bet['percentageWin'])

        Bet.insert(
            team = bet['team'],
            game_id = bet['gameId'],
            percentage_win = bet['percentageWin'],
            proportion = proportion,
            amount = size,
            date = datetime.datetime.now(),
            odds = bet['netOdds'],
            status = 0,
            account = 0,
            gameweek = bet['gameweek']
        )

# def get_bets(gameweek):
#     Bet.get(Bet.)

def get_bets():
    bets = Bet.get()
    return bets

def place_bets(week):
    Bet.update(status = 1).where(gameweek = week)

#checks nfldb for result and updates bet records/portfolio based on result
def checkForResult():
    return
