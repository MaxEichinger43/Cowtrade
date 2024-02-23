investment_dif_history = []
investment_history = []
def get_investment(capital_history: list, number: int, current_round: int) -> int:
    '''
    Contains the strategy of a player and returns the calculated value to invest, based on the input capital_list.
    '''
    global investment_dif_history
    enemy_number = (number + 1) % len(capital_history[0])
#-------------------------------------------------------
    if current_round == 0:
        investment = 10
        investment_old = investment
    else:
        enemy_investment_old = capital_history[current_round - 1][enemy_number] - capital_history[current_round][enemy_number]
        investment_dif = enemy_investment_old - investment_old
        investment_dif_history.append(investment_dif)
        print("invest_diff: ", investment_dif)

        if investment_dif > 0:
            print("erhöhe einsatz um diff")
            investment = investment_old + investment_dif + 1
        else:
            print("invest_old: ", investment_old)
            print("+1")
            investment = investment_old + 1
            print("investment: ", investment)

    investment_old = investment
    investment_history.append(investment_old)
    print("invest_hist: ", investment_history)
#-------------------------------------------------------
    return investment