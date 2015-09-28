def kelly_proportion(net_odds, prob_win):
    return (prob_win * (net_odds + 1) - 1) / net_odds

def kelly_size(net_odds, prob_win, bankroll):
    return kellyProportion(net_odds, prob_win) * bankroll


# assume 538 correct, betfair price out, calculate average profit for
# given edge, run 1000 times, calc mean and std dev

#loads of numpy in here
