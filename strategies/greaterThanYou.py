def get_investment(capital_history: list, number: int, current_round: int) -> int:
    '''
    Contains the strategy of a player and returns the calculated value to invest, based on the input capital_list.
    '''
    enemy_number = (number + 1) % len(capital_history[0]) # the number of the enemy. Example: Your number:1 -> enemy:0
#-------------------------------------------------------
    enemy_capital_old = capital_history[current_round - 1][enemy_number]
    enemy_capital_current = capital_history[current_round][enemy_number]

    if current_round == 0:
        enemy_investment_old = 0

    else:
        enemy_investment_old = enemy_capital_old - enemy_capital_current

    investment = enemy_investment_old + 1
#-------------------------------------------------------
    return investment