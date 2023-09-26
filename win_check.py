from playground import Playground
from constants import Winner
    

def convert_indexes_list_into_values_list(
    indexes_list: list[list[int]], 
    layout: list[str]
) -> list[list[str]]:
    values_list = []
    for indexes_list_element in indexes_list:
        values_list_element = [layout[index] for index in indexes_list_element]
        values_list.append(values_list_element)
    return values_list


def sum_playground_elements_values_lists(playground: Playground) -> list[list[str]]:
    rows_values_list = convert_indexes_list_into_values_list(
        playground.rows_indexes_list(), playground.layout)
    columns_values_list = convert_indexes_list_into_values_list(
        playground.columns_indexes_list(), playground.layout)
    diagonals_values_list = convert_indexes_list_into_values_list(
        playground.diagonals_indexes_list(), playground.layout)
    layout_elements_values_list = rows_values_list + columns_values_list + diagonals_values_list
    return layout_elements_values_list


def win_check(playground: Playground) -> Winner:
    layout_elements_values_list = sum_playground_elements_values_lists(playground)
    for layout_element in layout_elements_values_list: 
        user_streak, ai_streak = 0, 0
        if len(layout_element) < playground.win_streak:
            continue
        for value in layout_element:
            if value not in [playground.user_symbol, playground.ai_symbol]:
                user_streak, ai_streak = 0, 0
            elif value == playground.user_symbol:
                ai_streak = 0
                user_streak += 1
            else:
                user_streak = 0
                ai_streak += 1
            if user_streak == playground.win_streak:
                return Winner.USER
            elif ai_streak == playground.win_streak:
                return Winner.AI
    if playground.is_filled():
        return Winner.TIE
    return Winner.NONE
