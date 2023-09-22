import time


from constants import BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC, BRAINSTORM_ERROR_SEC
from playground import Playground
from ai import toggle_ai_brainstorm, generate_random_ai_move, output_ai_move


def test_toggle_ai_brainstorm() -> None:
    start_time = time.time()
    toggle_ai_brainstorm()
    runtime = time.time() - start_time
    assert runtime >= BRAINSTORM_MIN_SEC - BRAINSTORM_ERROR_SEC
    assert runtime <= BRAINSTORM_MAX_SEC + BRAINSTORM_ERROR_SEC


def test_generate_random_ai_move() -> None:
    test_playground = Playground(row_length = 3)
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


def count_filled_by_ai_boxes(playground: Playground) -> int:
    filled_by_ai_boxes = 0
    for box in playground.layout:
        if box == playground.ai_symbol:
            filled_by_ai_boxes += 1
    return filled_by_ai_boxes


def test_count_filled_by_ai_boxes() -> None:
    test_playground = Playground(row_length = 3)
    ai_symbol = test_playground.ai_symbol
    counts_for_playgrounds_map = [
        (['0', '1', '2', '3', '4', '5', '6', '7', '8'], 0),
        (['0', ai_symbol, ai_symbol, '3', '4', '5', '6', '7', '8'], 2),
        (['0', '1', ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol, '7', '8'], 5),
        ([ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol, ai_symbol, '6', '7', '8'], 6),
    ]
    for test_layout, filled_by_ai_count in counts_for_playgrounds_map:
        test_playground.layout = test_layout
        assert count_filled_by_ai_boxes(test_playground) == filled_by_ai_count
