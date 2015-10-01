import utilities.math_utilities as math_utilities
import utilities.nfldb_service as nfldb_service
from models.bet import Bet
from models.account import Account
import datetime

# print games for a given gameweek
def print_games(year, week):
    games = nfldb_service.gameweek_games()
    for game in games:
        print(game.gsis_id)
        print(game)
        # print(g.finished)
        # print(g.home_score)
        # print(g.away_score)

def calc_bets(data, week):
    bets = []
    games = nfldb_service.gameweek_games()
    for game in games:
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

def save_bets(bets):
    bankroll = Account.get().bankroll
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
def checkForResult(week):
    #update each bet to correct Status
    return
    #have finished flag on each game - so just run on all that have finished
    # profit = 0
    # # games for a given gameweek
    # get games we made a bet for
    # q.game(gsis_id = bet.gsis_id)
    # for g in q.as_games():
    # if(g.finished)
    # if(g.home_score > g.away_score)
    #
    # else
    #   away win
    #   if()
    # q.game(season_year=year, season_type='Regular', week=week)
    # for g in q.as_games():
    #     if(g.state = win)
    #         gameweek_bets[g.gsis_id]
    #         Bet.update({'state' = 3}).where(game_id = g.gsis_id)
    #         profit += gameweek_bets[g.gsis_id].amount * gameweek_bets[g.gsis_id].odds
    #     else
    #         Bet.update({'state' = 4}).where(game_id = g.gsis_id)
    #         profit -= gameweek_bets[g.gsis_id].amount
    #
    # Account.update({'bankroll': bankroll + profit}).where(id = 1)
