from playground import Playground


def read_user_input() -> str:
    user_input = input('Enter unfilled box number to make move or 0 to exit game: ')
    return user_input


def check_user_input(playground_size: int, raw_user_input: str) -> bool:
    try:
        user_input = int(raw_user_input.strip())
    except ValueError:
        return False
    if user_input in range(playground_size + 1):
        return True
    return False


def validate_user_move(playground: Playground, user_input: str) -> str:
    if not check_user_input(len(playground.layout), user_input):
        return 'Incorrect value.'
    elif int(user_input) and playground.layout[int(user_input) - 1] in playground.symbols_list():
        return 'This box is already filled.'
    return 'ok'


def fetch_valid_user_move(playground: Playground) -> int:
    while True:
        user_input = read_user_input()
        validation_message = validate_user_move(playground, user_input)
        if validation_message == 'ok':
            return int(user_input)
        else:
            print(validation_message, 'Please try again...')


def output_user_move(playground: Playground, user_move: int) -> Playground:
    playground.layout[user_move-1] = playground.user_symbol
    playground.draw_layout()
    print('Ok, got it! And now AI will make a move...')
    return playground
