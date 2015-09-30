import json
import logic.gameweek as gameweek

threshold = 0.04
bets = []
bankroll = 100

def main():
    with open("data/538.json") as data_file:
        data = json.load(data_file)

        for week in ["1","2", "3"]:
            gameweek_bets = gameweek.calc_bets(data, week, threshold)
            gameweek.save_bets(gameweek_bets, bankroll)
            bets.append(gameweek_bets)

        print(bets)

# multiple trials for a given edge, assuming mean error = 0
# for the bets selected, generate random outcome set, 1000 times, show mean winning, std dev
# graph outcome
#profit = 0
#x = 0
#results = []
#while x < 1000:
#    for bet in bets:
#        outcome = random.randint(0,100)
#        bet["percentageWin"] #how often they winning
#        if(outcome <= bet["percentageWin"]):
#            #won the bet
#            profit += bet["size"]
#        else:
#            profit -= bet["size"]

#    print profit
#    results.append(profit)
#    x += 1

#import random

#sum results / 1000
#print('mean profit: ', )
#print('std dev of profit')
#use matplotlib to graph results
#def rollDice():
#	roll = random.randint(1, 100)


#placed bets
# gameweek 1: 100units
# panthers 11.6 units @ 1.625 status: Won
# cardinals 23.5 units @ 0.8 status: Won
# 49ers 35.1 units @ 1.1 status: Won
# = +(1.625*11.6)+(23.5*0.8)+(35.1*1.1) = +74 units 74% roi
# week 2: 174 units

# gameweek 2: 174 units


# run from cmd
if __name__ == '__main__':
    app.run()
