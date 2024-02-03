capital_history = []

def get_investment(capital_list: list, number: int, current_round: int) -> int:
    '''
    Contains the strategy of a player and returns the calculated value to invest, based on the input capital_list.
    '''
    global capital_history
    enemy_number = (number + 1) % len(capital_list)
#-------------------------------------------------------

    if current_round == 0:
        capital_history.append((capital_list[0], capital_list[1]))
        enemy_investment_old = 0

    else:
        enemy_investment_old = capital_history[current_round - 1][enemy_number] - capital_history[current_round][enemy_number]

    print(capital_history)
    print(enemy_investment_old)
    investment = enemy_investment_old + 1

#-------------------------------------------------------
    capital_history.append(capital_list) # store current capital status
    return investment