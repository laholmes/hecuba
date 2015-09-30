import random
import numpy as np

def kelly_proportion(net_odds, prob_win):
    return (prob_win * (net_odds + 1) - 1) / net_odds

def kelly_size(net_odds, prob_win, bankroll):
    return kelly_proportion(net_odds, prob_win) * bankroll

def sharpe_ratio(expected_return, std_dev, risk_free):
    return (expected_return - risk_free) / std_dev

# use scipy to find npv of bets placed throughout season - take each week and discount return back
def npv():
    return
