from game.playground import Playground
from game.constants import PLAYGROUND_ROW_LENGTH
from game.user_move import check_user_input, validate_user_move


def test_check_user_input() -> None:
    check_results_for_tests_map = {
        'hello world': False,
        '': False,
        ' ': False,
        str(PLAYGROUND_ROW_LENGTH): True,
        '0': True,
        str(PLAYGROUND_ROW_LENGTH ** 2 + 1): False,
        str(PLAYGROUND_ROW_LENGTH ** 2): True,
    }
    for test_input, correct_result in check_results_for_tests_map.items():
        assert check_user_input(PLAYGROUND_ROW_LENGTH ** 2, test_input) == correct_result


def test_validate_user_move() -> None:
    test_playground = Playground(row_length=2)
    test_playground.layout[1] = test_playground.ai_symbol
    test_playground.layout[2] = test_playground.user_symbol
    check_results_for_tests_map = {
        'foo': 'Incorrect value.',
        '0': 'ok',
        '0': 'ok',
        '2': 'This box is already filled.',
        '3': 'This box is already filled.',
        '4': 'ok',
        '5': 'Incorrect value.',
    }
    for test_input, correct_result in check_results_for_tests_map.items():
        assert validate_user_move(test_playground, test_input) == correct_result
