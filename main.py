import exampleStrategy as strategy1
import exampleStrategy as strategy2

# Input parameters
STARTING_CAPITAL = 1000
ROUNDS = 10

# Init
strategy_capital = [STARTING_CAPITAL, STARTING_CAPITAL]
strategy_score = [0, 0]
strategy1_name = strategy1.__name__
strategy2_name = strategy2.__name__

# Loop for given amount of rounds
round = 0
while round < ROUNDS:
    points = 1              # define the raise in score upon win

    print(f"Points to win: {points}")
    print(f"Capitals: {strategy_capital}")
    
    strategy_investment1 = strategy1.get_investment(strategy_capital, 0)
    strategy_investment2 = strategy2.get_investment(strategy_capital, 1)
    
    print(f"Investments: {strategy_investment1}(S1) vs {strategy_investment2}(S2)")

    if strategy_investment1 > strategy_investment2:
        strategy_capital[0] -= strategy_investment1
        strategy_capital[1] -= strategy_investment2
        strategy_score[0] += points

        print(f"{strategy1_name} wins!")
    
    elif strategy_investment1 < strategy_investment2:
        strategy_capital[0] -= strategy_investment1
        strategy_capital[1] -= strategy_investment2
        strategy_score[1] += points

        print(f"{strategy2_name} wins!")

    
    else:
        #strategy_capital[0] -= strategy_investment1
        #strategy_capital[1] -= strategy_investment2
        pass

    print(f"Scores: {strategy_score[0]}(S1) to {strategy_score[1]}(S2)")
    print("-----------------------------------------------------\n-----------------------------------------------------")
    
    round += 1
    

    













#import os
#
## add strategies folder
#strategies_folder = "./strategies"
#
#STARTING_CAPITAL = 1000
#
#"""
#objects
#"""
#
#class Strategy:
#    def __init__(self) -> None:
#        self.capital = STARTING_CAPITAL
#        
#    def get_investment(self):
#        pass
#
#
#strategy_list = []
#
#
#"""
#import
#"""
#i = 0
## run through all files in the strategies-folder
#for strategy in os.listdir(strategies_folder):
#    if strategy.endswith(".py") and strategy != "__init__.py":
#        # get the name of the strategy from the filename without ".py"
#        strategy_name = os.path.splitext(strategy)[0]
#
#        try:
#            # try to import the strategy
#            exec(f"from strategies.{strategy_name} import *")
#            print(f"{strategy_name} importet correctly")
#
#        except ImportError:
#            print(f"{strategy_name} could not be importet")
#
#        strategy_name = Strategy()
#        strategy_list.append(strategy_name)
#        print("Capital: ",strategy_list[i].capital)
#        strategy_list[i].invest = strategy_list[i].get_investment()
#        print("Invest: ",strategy_list[i].invest)
#        i+=1
#
#
#def get_starting_capital(strategy_list):
#    pass