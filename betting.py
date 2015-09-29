import random
import numpy as np

def kelly_proportion(net_odds, prob_win):
    return (prob_win * (net_odds + 1) - 1) / net_odds

def kelly_size(net_odds, prob_win, bankroll):
    return kelly_proportion(net_odds, prob_win) * bankroll

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


def sharpe_ratio(expected_return, std_dev, risk_free):
    return (expected_return - risk_free) / std_dev
