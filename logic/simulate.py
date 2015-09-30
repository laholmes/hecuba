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
