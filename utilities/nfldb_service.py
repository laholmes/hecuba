# wrap access to nfldb
import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

def gameweek_games(year, week):
    return q.game(season_year=year, season_type='Regular', week=week).as_games()

def game(id):
    return q.game(season_year=year, season_type='Regular', week=week).as_games()
