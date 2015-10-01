import utilities.math_utilities as math_utilities
import utilities.nfldb_service as nfldb_service
from models.bet import Bet
from models.account import Account
import datetime

# print games for a given gameweek
# def print_games(year, week):
#     games = nfldb_service.gameweek_games()
#     for game in games:
#         print(game.gsis_id)
#         print(game)
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
                'away': 0,
                'gameId': g.gsis_id,
                'netOdds': betfairPriceHome,
                'percentageWin': homeTeamWeighting,
                'gameweek': week
            })

        if(betfairAwayPercentage + threshold <= awayTeamWeighting):
            bets.append({
                'away': 1,
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
    profit = 0
    bets = filter(lambda x: x.gameweek == week, get_bets())

    for bet in bets:
        game = nfldb_service.get_game(bet.game_id)
        if(game.finished)
            if(game.home_score > game.away_score)
                profit = update_profit(!bet.away).profit
                state = update_profit(!bet.away).state
            else
                profit = update_profit(bet.away).profit
                state = update_profit(bet.away).state

        Bet.update({'state': state}).where(game_id = g.gsis_id)

    Account.update({'bankroll': bankroll + profit}).where(id = 1)

def update_profit(won):
    profit = 0
    if (won)
        state = 3
        profit += gameweek_bets[game.gsis_id].amount * gameweek_bets[game.gsis_id].odds
    else
        state = 4
        profit -= gameweek_bets[game.gsis_id].amount

    return {'profit': profit, 'state': state}
