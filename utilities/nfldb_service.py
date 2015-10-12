# wrap access to nfldb

import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

def gameweek_games(year, week):
    return q.game(season_year=year, season_type='Regular', week=week).as_games()

def game(id):
    return q.game(gsis_id == id).as_games()

# print games for a given gameweek
def print_games(year, week):
    games = gameweek_games(year, week)
    for game in games:
        print(game.gsis_id)
        print(game)

print_games(2015, 6)
