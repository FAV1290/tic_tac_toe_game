from constants import PLAYGROUND_SIZE, PLAYABLE_SYMBOLS
from user_move import check_user_input, validate_user_move


def test_check_user_input() -> None:
    check_results_for_tests_map = {
        'hello world' : False,
        '' : False,
        ' ' : False,
        str(PLAYGROUND_SIZE) : True,
        '0' : True,
        str(PLAYGROUND_SIZE ** 2 + 1) : False,
        str(PLAYGROUND_SIZE ** 2) : True,
    }
    for test_input, correct_result in check_results_for_tests_map.items():
        assert check_user_input(test_input) == correct_result


def test_validate_user_move() -> None:
    test_playground = ['(1)', '(2)', PLAYABLE_SYMBOLS[0], '(4)']
    check_results_for_tests_map = {
        '0' : 'ok',
        'foo' : 'Incorrect value.',
        '3' : 'This box is already filled.',
        '4' : 'ok',
    }
    for test_input, correct_result in check_results_for_tests_map.items():
        assert validate_user_move(test_input, test_playground) == correct_result
