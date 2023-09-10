import random
import os
import time
import rich.console
import rich.table


from constants import PLATFORMS, ICONS, PLAYGROUND_SIZE, BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC


def clear_screen() -> None:
    os.system(PLATFORMS.get(os.name, ''))


def define_icons() -> tuple[str, str]:
    random.shuffle(ICONS)
    user_icon, ai_icon = ICONS[:2]
    return user_icon, ai_icon


def ai_makes_first_turn() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(random.randint(BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC))


def check_user_input(raw_user_input: str) -> bool:
    try:
        user_input = int(raw_user_input.strip())
    except ValueError:
        return False
    if user_input in range(PLAYGROUND_SIZE ** 2 + 1):
        return True
    return False


def get_default_playground() -> list[str]:
    default_playground = []
    for item in range(PLAYGROUND_SIZE ** 2):
        default_playground.append(f'({item + 1})')
    return default_playground


def draw_current_playground(playground: list[str]) -> None:
    table = rich.table.Table(show_header = False)
    console = rich.console.Console()
    for index in range(0, PLAYGROUND_SIZE ** 2, PLAYGROUND_SIZE):
        table.add_row(playground[index], playground[index + 1], playground[index + 2])
    clear_screen()    
    console.print(table)


def get_user_turn(playground: list[str], user_icon: str, ai_icon: str) -> int:
    while True:
        user_input = input('Enter unfilled box number to make turn or 0 to exit game: ')
        if not check_user_input(user_input):
            print('Incorrect value. Please try again...')
        elif int(user_input) and playground[int(user_input)-1] in [user_icon, ai_icon]:
            print('This box is already filled. Please try again...')
        else:
            return int(user_input)
        

def get_random_ai_turn(playground: list[str], user_icon: str, ai_icon: str) -> int:
    ai_turn = None
    while ai_turn is None or playground[ai_turn] in [user_icon, ai_icon]:
        ai_turn = random.randint(0, PLAYGROUND_SIZE ** 2 - 1)
    return ai_turn


def make_ai_turn(playground: list[str], user_icon: str, ai_icon: str) -> list[str]:
    toggle_ai_brainstorm()
    ai_turn = get_random_ai_turn(playground, user_icon, ai_icon)
    playground[ai_turn] = ai_icon
    draw_current_playground(playground)
    print('Done! Your turn now...')
    return playground


def main() -> None:
    user_icon, ai_icon = define_icons()
    playground = get_default_playground()
    game_on = True
    draw_current_playground(playground)
    print(f'Game on! Your icon is {user_icon}, AI icon is {ai_icon}', end=' ')
    
    if ai_makes_first_turn():
        print('AI makes the first turn! Please wait a sec...')
        playground = make_ai_turn(playground, user_icon, ai_icon)
    else:
        print('You make the first turn!')
    while game_on:
        user_turn = get_user_turn(playground, user_icon, ai_icon)
        if not user_turn:
            game_on = False
            continue
        playground[user_turn-1] = user_icon
        draw_current_playground(playground)
        print("Ok. And now AI will make it's turn...")
        playground = make_ai_turn(playground, user_icon, ai_icon)
        

if __name__ == '__main__':
    main()