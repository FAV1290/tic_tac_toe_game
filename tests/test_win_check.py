from game.enums import Winner
from game.playground import Playground
from game.win_check import (
    is_suitable_for_win_streak,
    win_check, check_if_winner_defined,
    convert_indexes_list_into_values_list,
    sum_playground_elements_values_lists,
)


def test_convert_indexes_list_into_values_list() -> None:
    layout = [
        '(0)', '(1)', '(2)', '(3)',
        '(4)', '(5)', '(6)', '(7)',
        '(8)', '(9)', '(10)', '(11)',
        '(12)', '(13)', '(14)', '(15)',
    ]
    indexes_lists = [
        [[1], [2], [15], [3]],
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        [[15, 5], [10, 2]],
    ]
    correct_answers = [
        [['(1)'], ['(2)'], ['(15)'], ['(3)']],
        [['(0)', '(1)', '(2)'], ['(3)', '(4)', '(5)'], ['(6)', '(7)', '(8)']],
        [['(15)', '(5)'], ['(10)', '(2)']],
    ]
    for index in range(len(indexes_lists)):
        test_answer = convert_indexes_list_into_values_list(indexes_lists[index], layout)
        correct_answer = correct_answers[index]
        assert test_answer == correct_answer


def test_sum_playground_elements_values_lists() -> None:
    correct_answer = [
        ['(0)', '(1)'], ['(2)', '(3)'],
        ['(0)', '(2)'], ['(1)', '(3)'],
        ['(0)'], ['(1)', '(2)'], ['(3)'], ['(0)', '(3)'], ['(1)'], ['(2)'],
    ]
    test_playground = Playground(row_length=2, numerate_from=0)
    assert sum_playground_elements_values_lists(test_playground) == correct_answer


def test_is_suitable_for_win_streak() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layout_elements_and_results = [
        (['1', '2', '3'], True),
        ([user_symbol, user_symbol, '3'], True),
        (['1', ai_symbol, ai_symbol, '4'], True),
        ([ai_symbol, ai_symbol, user_symbol], False),
        ([user_symbol, user_symbol, ai_symbol, user_symbol], False),
        ([user_symbol, user_symbol, ai_symbol, '4'], False),
        ([user_symbol, user_symbol, ai_symbol, '4', '5'], True),
        (['1', '2'], False),
    ]
    for layout_element, result in layout_elements_and_results:
        assert is_suitable_for_win_streak(layout_element, test_playground) == result


def test_check_if_winner_defined() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layout_elements_and_winners = [
        (['1', '2', '3'], None),
        ([user_symbol, user_symbol, user_symbol], Winner.USER),
        ([ai_symbol, ai_symbol, ai_symbol, '4'], Winner.AI),
        ([ai_symbol, ai_symbol, user_symbol], None),
        ([user_symbol, user_symbol, ai_symbol, user_symbol], None),
        (['1', user_symbol, user_symbol, user_symbol, '5'], Winner.USER),
        ([user_symbol, user_symbol, ai_symbol, '4', '5'], None),
        ([ai_symbol, ai_symbol], None),
    ]
    for layout_element, winner in layout_elements_and_winners:
        assert check_if_winner_defined(layout_element, test_playground) == winner


def test_win_check() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    test_params_list = [
        (['1', '2', '3', '4'], 2, 2, None),
        ([ai_symbol, ai_symbol, '3', '4'], 2, 2, Winner.AI),
        ([user_symbol, '2', '3', user_symbol], 2, 2, Winner.USER),
        (['1', user_symbol, ai_symbol, '4'], 2, 2, None),
        ([ai_symbol, ai_symbol, ai_symbol, ai_symbol], 2, 2, Winner.AI),
        ([ai_symbol, '2', ai_symbol, '4'], 2, 2, Winner.AI),
        ([user_symbol, user_symbol, user_symbol, '4', '5', '6', '7', '8', '9'], 3, 3, Winner.USER),
        (['1', ai_symbol, '3', '4', ai_symbol, '6', '7', ai_symbol, '9'], 3, 3, Winner.AI),
        (['1', '2', user_symbol, '4', user_symbol, '6', user_symbol, '8', '9'], 3, 3, Winner.USER),
        ([user_symbol, user_symbol, '3', user_symbol, '5', '6', '7', '8', '9'], 3, 3, None),
        ([
            '1', ai_symbol, user_symbol,
            user_symbol, ai_symbol, ai_symbol,
            ai_symbol, user_symbol, user_symbol,
        ], 3, 3, Winner.TIE),
        ([
            ai_symbol, user_symbol, ai_symbol,
            user_symbol, ai_symbol, user_symbol,
            user_symbol, ai_symbol, user_symbol,
        ], 3, 3, Winner.TIE),
        (['1', '2', ai_symbol, '4', ai_symbol, '6', '7', '8', '9'], 3, 2, Winner.AI),
        ([user_symbol, '2', '3', '4', '5', '6', user_symbol, '8', '9'], 3, 2, None),
        (['1', '2', '3', user_symbol, '5', '6', user_symbol, '8', '9'], 3, 2, Winner.USER),
    ]
    for test_params in test_params_list:
        layout, row_length, win_streak, correct_result = test_params
        test_playground.layout = layout
        test_playground.row_length = row_length
        test_playground.win_streak = win_streak
        assert win_check(test_playground) == correct_result
