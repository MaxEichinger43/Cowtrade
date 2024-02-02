capital_history = []
def get_investment(capital_list: list, number: int) -> int:
    '''
    Contains the strategy of a player and returns the calculated value to invest, based on the input capital_list.
    '''
    global capital_history

    capital_history.append(capital_list) # store all transactions indirectly in the capital-history

    the_other = (number + 1) % len(capital_list)
    print(the_other)
    investment = capital_list[the_other] + 1
    return investment