import json
import logic.gameweek as gameweek

bets = []

def main():
    with open("data/538.json") as data_file:
        data = json.load(data_file)

        for week in ["1","2","3"]:
            gameweek_bets = gameweek.calc_bets(data, week)
            gameweek.save_bets(gameweek_bets)
            bets.append(gameweek_bets)

        print(bets)

# run from cmd
if __name__ == '__main__':
    app.run()
