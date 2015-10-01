def simulate(bet, simulations, iterations)
    returns = []
    wins = 0
    simulation = 0
    iteration = 0

    while(simulation < simulations):
        balance = 0
        while(iteration < iterations):
            # effectively assuming uniform dist
            result = random.random()
            if(result <= bet.percentage_win) {
                # win
                wins += 1
                balance += bet.odds * bet.amount
            } else {
                balance -= bet.amount
            }
            iteration+=1
        returns[simulation] = balance
        simulation+=1

    std = np.std(returns)
    var = np.var(returns)
    mean = np.mean(returns)

    print(returns)

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
