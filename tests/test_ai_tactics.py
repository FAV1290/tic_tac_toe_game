from game.playground import Playground
from game.ai_tactics import (
    sum_playground_elements_indexes_lists, create_win_streak_slices_list, find_notable_indexes)


def test_sum_playground_elements_indexes_lists() -> None:
    row_length_to_elements_list_map = {
        2: [[0, 1], [2, 3], [0, 2], [1, 3], [0], [1, 2], [3], [0, 3], [1], [2]],
        3: [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0], [1, 3], [2, 4, 6], [5, 7], [8],
            [0, 4, 8], [1, 5], [2], [3, 7], [6],
        ],
    }
    for row_length, expected_elements in row_length_to_elements_list_map.items():
        test_playground = Playground(row_length=row_length)
        assert sum_playground_elements_indexes_lists(test_playground) == expected_elements


def test_create_win_streak_slices_list() -> None:
    test_playground = Playground(row_length=3)
    win_streak_to_slices_map = {
        3: [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [2, 4, 6], [0, 4, 8],
        ],
        2: [
            [0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8],
            [0, 3], [3, 6], [1, 4], [4, 7], [2, 5], [5, 8],
            [1, 3], [2, 4], [4, 6], [5, 7],
            [0, 4], [4, 8], [1, 5], [3, 7],
        ],
    }
    for win_streak, expected_slices in win_streak_to_slices_map.items():
        test_playground.win_streak = win_streak
        assert create_win_streak_slices_list(test_playground) == expected_slices


def test_find_winning_indexes() -> None:
    test_playground = Playground(row_length=3, win_streak=3, numerate_from=0)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_expected_indexes = [
        (['(0)', '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)'], None),
        ([ai_symbol, ai_symbol, '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)'], [2]),
        ([
            user_symbol, ai_symbol, user_symbol,
            ai_symbol, user_symbol, ai_symbol,
            user_symbol, ai_symbol, user_symbol,
        ], None),
        ([user_symbol, ai_symbol, '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)'], None),
        (['(0)', '(1)', ai_symbol, '(3)', ai_symbol, '(5)', '(6)', '(7)', '(8)'], [6]),
        ([ai_symbol, ai_symbol, '(2)', ai_symbol, '(4)', '(5)', '(6)', '(7)', '(8)'], [2, 6]),
        (
            ['(0)', ai_symbol, ai_symbol, ai_symbol, '(4)', '(5)', ai_symbol, '(7)', '(8)'],
            [0, 0, 4],
        ),
        ([ai_symbol, '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', ai_symbol], [4]),
        ([user_symbol, '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', user_symbol], None),
        (
            ['(0)', ai_symbol, '(2)', ai_symbol, ai_symbol, ai_symbol, '(6)', ai_symbol, '(8)'],
            None,
        ),
    ]
    for layout, expected_indexes in layouts_and_expected_indexes:
        test_playground.layout = layout
        assert find_notable_indexes(test_playground)['winning'] == expected_indexes


def test_find_check_breaking_indexes() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_expected_results = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8'], None),
        ([user_symbol, ai_symbol, '2', user_symbol, user_symbol, '5', '6', '7', '8'], [5, 6, 8]),
        (['0', '1', user_symbol, '3', user_symbol, '5', '6', '7', '8'], [6]),
        ([user_symbol, user_symbol, '2', user_symbol, '4', '5', '6', '7', '8'], [2, 6]),
        ([user_symbol, user_symbol, user_symbol, '3', '4', '5', '6', user_symbol, '8'], [4]),
        ([user_symbol, ai_symbol, user_symbol, '3', '4', '5', '6', user_symbol, '8'], None),
    ]
    for layout, expected_result in layouts_and_expected_results:
        test_playground.layout = layout
        assert find_notable_indexes(test_playground)['defensive'] == expected_result


def test_find_suitable_for_offence_indexes() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_expected_results = [
        (
            [ai_symbol, user_symbol, '2', ai_symbol, ai_symbol, '5', '6', '7', '8'],
            [2, 2, 5, 5, 6, 6, 6, 7, 8, 8, 8],
        ),
        (
            ['0', '1', ai_symbol, '3', ai_symbol, '5', '6', user_symbol, '8'],
            [0, 0, 0, 1, 3, 3, 5, 5, 6, 6, 8, 8],
        ),
        (
            [ai_symbol, ai_symbol, '2', ai_symbol, '4', '5', '6', user_symbol, user_symbol],
            [2, 2, 4, 4, 5, 6, 6],
        ),
        (
            [ai_symbol, ai_symbol, ai_symbol, '3', user_symbol, '5', '6', ai_symbol, '8'],
            [3, 5, 6, 6, 8, 8],
        ),
    ]
    for layout, expected_result in layouts_and_expected_results:
        test_playground.layout = layout
        offensive_indexes = find_notable_indexes(test_playground)['offensive']
        if offensive_indexes is not None:
            assert sorted(offensive_indexes) == expected_result
        else:
            assert expected_result is None
