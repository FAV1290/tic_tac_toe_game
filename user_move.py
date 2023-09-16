from constants import PLAYABLE_SYMBOLS, PLAYGROUND_SIZE
from playground import draw_playground


def read_user_input() -> str:
    user_input = input('Enter unfilled box number to make move or 0 to exit game: ')
    return user_input


def check_user_input(raw_user_input: str) -> bool:
    try:
        user_input = int(raw_user_input.strip())
    except ValueError:
        return False
    if user_input in range(PLAYGROUND_SIZE ** 2 + 1):
        return True
    return False


def validate_user_move(user_input: str, playground: list[str]) -> str:
    if not check_user_input(user_input):
        return 'Incorrect value.'
    elif int(user_input) and playground[int(user_input) - 1] in PLAYABLE_SYMBOLS:
        return 'This box is already filled.'
    return 'ok'


def fetch_valid_user_move(playground: list[str]) -> int:
    while True:
        user_input = read_user_input()
        validation_message = validate_user_move(user_input, playground)
        if validation_message == 'ok':
            return int(user_input)
        else:
            print(validation_message, 'Please try again...')


def output_user_move(playground: list[str], user_symbol: str, user_move: int) -> list[str]:
    playground[user_move-1] = user_symbol
    draw_playground(playground)
    print('Ok, got it! And now AI will make a move...')
    return playground
