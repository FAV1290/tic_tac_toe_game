import time


from game.ai_move import (
    toggle_ai_brainstorm,
    generate_random_ai_move,
    generate_winning_ai_move,
    generate_defensive_ai_move,
    generate_offensive_ai_move
)
from game.playground import Playground
from game.constants import BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC, BRAINSTORM_ERROR_SEC


def test_toggle_ai_brainstorm() -> None:
    start_time = time.time()
    toggle_ai_brainstorm()
    runtime = time.time() - start_time
    assert runtime >= BRAINSTORM_MIN_SEC - BRAINSTORM_ERROR_SEC
    assert runtime <= BRAINSTORM_MAX_SEC + BRAINSTORM_ERROR_SEC


def test_generate_winning_ai_move() -> None:
    test_playground = Playground(row_length=3, win_streak=3, numerate_from=0)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_expected_moves = [
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
        (['(0)', ai_symbol, ai_symbol, ai_symbol, '(4)', '(5)', ai_symbol, '(7)', '(8)'], [0]),
        ([ai_symbol, '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', ai_symbol], [4]),
        ([user_symbol, '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', user_symbol], None),
        (
            ['(0)', ai_symbol, '(2)', ai_symbol, ai_symbol, ai_symbol, '(6)', ai_symbol, '(8)'],
            None,
        ),
    ]
    for layout, expected_moves in layouts_and_expected_moves:
        test_playground.layout = layout
        ai_move = generate_winning_ai_move(test_playground)
        if expected_moves is None:
            assert ai_move is None
        else:
            assert ai_move in expected_moves


def test_generate_defensive_ai_move() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_acceptable_moves = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8'], None),
        ([user_symbol, ai_symbol, '3', user_symbol, user_symbol, '5', '6', '7', '8'], [5, 6, 8]),
        (['0', '1', user_symbol, '3', user_symbol, '5', '6', '7', '8'], [6]),
        ([user_symbol, user_symbol, '2', user_symbol, '4', '5', '6', '7', '8'], [2, 6]),
        ([user_symbol, user_symbol, user_symbol, '3', '4', '5', '6', user_symbol, '8'], [4]),
        ([user_symbol, ai_symbol, user_symbol, '3', '4', '5', '6', user_symbol, '8'], None),
    ]
    for layout, acceptable_moves in layouts_and_acceptable_moves:
        test_playground.layout = layout
        ai_move = generate_defensive_ai_move(test_playground)
        if acceptable_moves is None:
            assert ai_move is None
        else:
            assert ai_move in acceptable_moves


def test_generate_offensive_ai_move() -> None:
    test_playground = Playground(row_length=3, win_streak=3)
    user_symbol = test_playground.user_symbol
    ai_symbol = test_playground.ai_symbol
    layouts_and_acceptable_moves = [
        ([ai_symbol, user_symbol, '2', ai_symbol, ai_symbol, '5', '6', '7', '8'], [6, 8]),
        (['0', '1', ai_symbol, '3', ai_symbol, '5', '6', user_symbol, '8'], [0]),
        (
            [ai_symbol, ai_symbol, '2', ai_symbol, '4', '5', '6', user_symbol, user_symbol],
            [2, 4, 6],
        ),
        ([ai_symbol, ai_symbol, ai_symbol, '3', user_symbol, '5', '6', ai_symbol, '8'], [6, 8]),
    ]
    for layout, acceptable_moves in layouts_and_acceptable_moves:
        test_playground.layout = layout
        assert generate_offensive_ai_move(test_playground) in acceptable_moves


def test_generate_random_ai_move() -> None:
    test_playground = Playground(row_length=3)
    filler = test_playground.symbols_list()[0]
    answers_for_playgrounds_map = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8'], [0, 1, 2, 3, 4, 5, 6, 7, 8]),
        ([filler, filler, filler, filler, '4', '5', '6', '7', '8'], [4, 5, 6, 7, 8]),
        (['0', '1', filler, filler, filler, filler, filler, filler, filler], [0, 1]),
        ([filler, filler, filler, filler, filler, filler, filler, filler, filler], None),
    ]
    for test_layout, possible_answers in answers_for_playgrounds_map:
        test_playground.layout = test_layout
        ai_move = generate_random_ai_move(test_playground)
        if possible_answers is not None:
            assert ai_move in possible_answers
        else:
            assert ai_move is None
