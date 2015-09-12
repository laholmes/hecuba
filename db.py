import sqlite3

conn = sqlite3.connect('hecuba.db')
c = conn.cursor()

c.execute('''CREATE TABLE Team
             (id INTEGER, name TEXT)''')

multi_lines = [ (1, 'San Francisco 49ers'),
               (2, 'Chicago Bears'),
               (3, 'Cincinnati Bengals'),
               (4, 'Buffalo Bills'),
               (5, 'Denver Broncos'),
               (6, 'Cleveland Browns'),
               (7, 'Tampa Bay Buccaneers'),
               (8, 'Arizona Cardinals'),
               (9, 'San Diego Chargers'),
               (10, 'Kansas City Chiefs'),
               (11, 'Indianapolis Colts'),
               (12, 'Dallas Cowboys'),
               (13, 'Miami Dolphins'),
               (14, 'Philadelphia Eagles'),
               (15, 'Atlanta Falcons'),
               (16, 'New York Giants'),
               (17, 'Jacksonville Jaguars'),
               (18, 'New York Jets'),
               (19, 'Detroit Lions'),
               (20, 'Green Bay Packers'),
               (21, 'Carolina Panthers'),
               (22, 'New England Patriots'),
               (23, 'Oakland Raiders'),
               (24, 'St.Louis Rams'),
               (25, 'Baltimore Ravens'),
               (26, 'Washington Redskins'),
               (27, 'New Orleans Saints'),
               (28, 'Seattle Seahawks'),
               (29, 'Pittsburgh Steelers'),
               (30, 'Houston Texans'),
               (31, 'Tennesse Titans'),
               (32, 'Minnesota Vikings')]

c.executemany('INSERT INTO Team VALUES (?,?)', multi_lines)

for row in c.execute('SELECT * FROM Team'):
        print row

conn.commit()
conn.close()
