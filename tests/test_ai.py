import time


from constants import (
    BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC, BRAINSTORM_ERROR_SEC, PLAYABLE_SYMBOLS)
from ai import toggle_ai_brainstorm, generate_random_ai_move, output_ai_move


def test_toggle_ai_brainstorm() -> None:
    start_time = time.time()
    toggle_ai_brainstorm()
    runtime = time.time() - start_time
    assert runtime >= BRAINSTORM_MIN_SEC - BRAINSTORM_ERROR_SEC
    assert runtime <= BRAINSTORM_MAX_SEC + BRAINSTORM_ERROR_SEC


def test_generate_random_ai_move() -> None:
    user_symbol, ai_symbol = PLAYABLE_SYMBOLS
    answers_for_playgrounds_map = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8'], [0, 1, 2, 3, 4, 5, 6, 7, 8]),
        ([user_symbol, ai_symbol, ai_symbol, ai_symbol, '4', '5', '6', '7', '8'], [4, 5, 6, 7, 8]),
        (['0', '1', ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol], [0, 1]),
        ([user_symbol, ai_symbol, ai_symbol, user_symbol], None),
    ]
    for playground, possible_answers in answers_for_playgrounds_map:
        ai_move = generate_random_ai_move(playground, user_symbol, ai_symbol)
        if possible_answers is not None:
            assert ai_move in possible_answers
        else:
            assert ai_move is None


def count_filled_by_ai_boxes(playground: list[str] | None, ai_symbol: str) -> int:
    if playground is None:
        return -1
    filled_by_ai_boxes = 0
    for box in playground:
        if box == ai_symbol:
            filled_by_ai_boxes += 1
    return filled_by_ai_boxes


def test_count_filled_by_ai_boxes() -> None:
    ai_symbol = 'X'
    counts_for_playgrounds_map = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 0),
        (['0', ai_symbol, ai_symbol, '3', '4', '5', '6', '7', '8', '9'], 2),
        (['0', '1', ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol], 5),
        ([ai_symbol, ai_symbol, ai_symbol, ai_symbol], 4),
        (None, -1),
    ]
    for playground, filled_by_ai_count in counts_for_playgrounds_map:
        assert count_filled_by_ai_boxes(playground, ai_symbol) == filled_by_ai_count


def test_output_ai_move() -> None:
    user_symbol = 'X'
    ai_symbol = 'O'
    counts_for_playgrounds_map = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1),
        ([user_symbol, ai_symbol, ai_symbol, user_symbol, '4', '5', '6', '7', '8', '9'], 3),
        (['0', '1', ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol], 6),
        ([user_symbol, ai_symbol, ai_symbol, user_symbol], -1),
    ]
    for playground, correct_count in counts_for_playgrounds_map:
        new_playground = output_ai_move(playground, user_symbol, ai_symbol)
        assert count_filled_by_ai_boxes(new_playground, ai_symbol) == correct_count
