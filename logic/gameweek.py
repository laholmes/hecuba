import utilities.math_utilities as math_utilities
import utilities.nfldb_service as nfldb_service
from models.bet import Bet
from models.account import Account
import datetime

account = Account.select().where(Account.id == 1).first()

def calc_bets(data, week):
    bets = []
    games = nfldb_service.gameweek_games(2015, week)
    for game in games:
        game_price_data = data['weeks'][week]['games'][game.gsis_id]
        betfairPriceHome = game_price_data['betfairPriceHome']
        betfairPriceAway = game_price_data['betfairPriceAway']
        homeTeamWeighting = game_price_data['homeTeamWeighting']
        awayTeamWeighting = game_price_data['awayTeamWeighting']

        betfairHomePercentage = 1.0 / (betfairPriceHome + 1)
        betfairAwayPercentage = 1.0 / (betfairPriceAway + 1)

        if(betfairHomePercentage + account.threshold <= homeTeamWeighting):
            bets.append({
                'away': 0,
                'gameId': game.gsis_id,
                'netOdds': betfairPriceHome,
                'percentageWin': homeTeamWeighting,
                'gameweek': week
            })

        if(betfairAwayPercentage + account.threshold <= awayTeamWeighting):
            bets.append({
                'away': 1,
                'gameId': game.gsis_id,
                'netOdds': betfairPriceAway,
                'percentageWin': awayTeamWeighting,
                'gameweek': week
            })
    return bets

def save_bets(bets):
    bankroll = account.bankroll
    for bet in bets:
        size = math_utilities.kelly_size(bet['netOdds'], bet['percentageWin'], bankroll)
        proportion = math_utilities.kelly_proportion(bet['netOdds'], bet['percentageWin'])

        Bet.insert(
            away = bet['away'],
            game_id = bet['gameId'],
            percentage_win = bet['percentageWin'],
            proportion = proportion,
            amount = size,
            date = datetime.datetime.now(),
            odds = bet['netOdds'],
            status = 0,
            account = 0,
            gameweek = bet['gameweek']
        ).execute()

def get_bets(week):
    bets = Bet.select().where(Bet.gameweek == week).execute()
    return bets

def place_bets(week):
    Bet.update(status = 1).where(gameweek = week)

#checks nfldb for result and updates bet records/portfolio based on result
def check_for_result(week):
    profit = 0
    bets = get_bets(week)
    print(bets)
    # bets = filter(lambda x: x.gameweek == week, get_bets())

    for bet in bets:
        game = nfldb_service.game(bet.game_id)
        if(game.finished):
            if(game.home_score > game.away_score):
                profit = update_profit(bet.away == False).profit
                state = update_profit(bet.away == True).state
            else:
                profit = update_profit(bet.away).profit
                state = update_profit(bet.away).state

        Bet.update({'state': state}).where(game_id = game.gsis_id).execute()

    Account.update({'bankroll': bankroll + profit}).where(id = 1).execute()

def update_profit(won):
    profit = 0
    if(won):
        state = 3
        profit += gameweek_bets[game.gsis_id].amount * gameweek_bets[game.gsis_id].odds
    else:
        state = 4
        profit -= gameweek_bets[game.gsis_id].amount

    return {'profit': profit, 'state': state}
