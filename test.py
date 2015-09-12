import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2015, season_type='Regular', week=1)
# for pp in q.sort('passing_yds').limit(10).as_aggregate():
#     print pp.player, pp.passing_yds
for g in q.as_games():
    print g



# filtering
# returns all games in a gameweek with edge (538 vs betfair price) > threshold


# constructs list of bets for week with edge
