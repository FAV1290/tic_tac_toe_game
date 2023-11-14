from game.enums import Winner
from game.playground import Playground


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


def is_suitable_for_win_streak(layout_element: list[str], playground: Playground) -> bool:
    hypothetic_user_streak, hypothetic_ai_streak = 0, 0
    for value in layout_element:
        if value == playground.user_symbol:
            hypothetic_ai_streak = 0
            hypothetic_user_streak += 1
        elif value == playground.ai_symbol:
            hypothetic_user_streak = 0
            hypothetic_ai_streak += 1
        else:
            hypothetic_user_streak += 1
            hypothetic_ai_streak += 1
        if playground.win_streak in [hypothetic_user_streak, hypothetic_ai_streak]:
            return True
    return False


def check_if_winner_defined(layout_element: list[str], playground: Playground) -> Winner | None:
    user_streak, ai_streak = 0, 0
    for value in layout_element:
        if value not in playground.symbols_list():
            user_streak, ai_streak = 0, 0
        elif value == playground.user_symbol:
            ai_streak, user_streak = 0, user_streak + 1
        else:
            user_streak, ai_streak = 0, ai_streak + 1
        if user_streak == playground.win_streak:
            return Winner.USER
        if ai_streak == playground.win_streak:
            return Winner.AI
    return None


def win_check(playground: Playground) -> Winner | None:
    win_possibilities_count = 0
    for layout_element in sum_playground_elements_values_lists(playground):
        if len(layout_element) < playground.win_streak:
            continue
        winner = check_if_winner_defined(layout_element, playground)
        if winner is not None:
            return winner
        if is_suitable_for_win_streak(layout_element, playground):
            win_possibilities_count += 1
    if not win_possibilities_count:
        return Winner.TIE
    return None
