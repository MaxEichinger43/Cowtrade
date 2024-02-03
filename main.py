import os
import matplotlib.pyplot as plt

# ---INPUT PARAMETERS---
# change the "import -->name<-- as" to the strategies you want
from strategies import greaterThanYou as strategy1
from strategies import exampleStrategy as strategy2

# capital and round count can be changed
STARTING_CAPITAL = 1000
ROUNDS = 100
plot = True

# init
strategy_capital = [STARTING_CAPITAL, STARTING_CAPITAL]
capital_history = []
strategy_points = [0, 0]
strategy_score = [0, 0]
strategy1_name = os.path.splitext(os.path.basename(strategy1.__file__))[0]
strategy2_name = os.path.splitext(os.path.basename(strategy2.__file__))[0]

# loop for given amount of rounds
print("-----------------------------------------------------\nStarting program\n-----------------------------------------------------")
for round in range(ROUNDS):
    print(f"Round: {round + 1}\n-----------------------------------------------------")
    capital_history.append((strategy_capital[0],strategy_capital[1]))

    # define the raise in score upon win
    points = 1

    print(f"Points to win: {points}")
    print(f"Capitals:\n    {strategy1_name}: {strategy_capital[0]}\n    {strategy2_name}: {strategy_capital[1]}")
    
    strategy_investment1 = abs(strategy1.get_investment(capital_history, 0, round))
    strategy_investment2 = abs(strategy2.get_investment(capital_history, 1, round))
    if strategy_capital[0] - strategy_investment1 < 0:
        strategy_investment1 = 0
    if strategy_capital[1] - strategy_investment2 < 0:
        strategy_investment2 = 0
    
    print(f"Investments:\n    {strategy1_name}: {strategy_investment1}\n    {strategy2_name}: {strategy_investment2}")

    # check who wins
    if strategy_investment1 > strategy_investment2:
        strategy_capital[0] -= strategy_investment1
        strategy_capital[1] -= strategy_investment2
        strategy_points[0] += points
        strategy_score[0] += 1
        print(f"\n{strategy1_name} wins!")
    
    elif strategy_investment1 < strategy_investment2:
        strategy_capital[0] -= strategy_investment1
        strategy_capital[1] -= strategy_investment2
        strategy_points[1] += points
        strategy_score[1] += 1
        print(f"\n{strategy2_name} wins!")

    else:
        #strategy_capital[0] -= strategy_investment1
        #strategy_capital[1] -= strategy_investment2
        pass

    # update the capital-list
    strategy_capital = [strategy_capital[0],strategy_capital[1]]

    print(f"\nScore:\n    {strategy1_name}: {strategy_score[0]}\n    {strategy2_name}: {strategy_score[1]}")
    print("-----------------------------------------------------")


# Show results
print("\n_____________________________________________________\n-Results-\n")
print(f"{strategy1_name} won {strategy_score[0]} times and {strategy_points[0]} points!")
print(f"{strategy2_name} won {strategy_score[1]} times and {strategy_points[1]} points!")
print("_____________________________________________________\n")

def plot_results(ROUNDS, capital_history, strategy1_name, strategy2_name):
    rounds = list(range(1, ROUNDS + 1))
    plt.figure(figsize=(10, 6))

# Plotting Player 1's capital over rounds
    plt.plot(rounds, [capital[0] for capital in capital_history], label=f"{strategy1_name}'s Capital", marker='o')

# Plotting Player 2's capital over rounds
    plt.plot(rounds, [capital[1] for capital in capital_history], label=f"{strategy2_name}'s Capital", marker='o')

    plt.title('Capital Over Rounds')
    plt.xlabel('Rounds')
    plt.ylabel('Capital')
    plt.legend()
    plt.grid(True)
    plt.show()

if plot:
    # Plotting the results
    plot_results(ROUNDS, capital_history, strategy1_name, strategy2_name)
