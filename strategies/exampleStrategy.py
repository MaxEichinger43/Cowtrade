capital_history = []

def get_investment(capital_list: list, number: int, current_round: int) -> int:
    '''
    Contains the strategy of a player and returns the calculated value to invest, based on the input capital_list.
    '''
    global capital_history
    enemy_number = (number + 1) % len(capital_list)
#-------------------------------------------------------



    #put strategy here
    investment = 42



#-------------------------------------------------------
    capital_history.append(capital_list) # store current capital status
    return investment