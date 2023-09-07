import random
import os
import time
import rich.console
import rich.table


def clear_screen() -> None:
    platforms = {
        'nt' : 'cls',
        'posix' : 'clear',
    }
    _ = os.system(platforms.get(os.name, ''))


def define_icons() -> tuple[str, str]:
    user_icon = random.choice(['\u274c', '\u2b55'])
    if user_icon == '\u274c':
        ai_icon = '\u2b55'
    else:
        ai_icon = '\u274c'
    return user_icon, ai_icon


def check_user_input(raw_user_input: str) -> bool:
    try:
        user_input = int(raw_user_input.strip())
    except ValueError:
        return False
    if 0 <= user_input < 10:
        return True
    return False


def get_user_turn(playground: list[str], user_icon: str, ai_icon: str) -> int:
    try:
        user_input = input('Enter unfilled box number to make turn or 0 to exit game: ')
    except RecursionError:
        print('\rAre you kidding me? Too many incorrect values. The game will now shutdown')
        return 0
    if not check_user_input(user_input):
        print('Incorrect value. Please try again...')
        return get_user_turn(playground, user_icon, ai_icon)
    if playground[int(user_input)-1] in [user_icon, ai_icon]: 
        print('This box is not empty. Please try again...')
        return get_user_turn(playground, user_icon, ai_icon)   
    return int(user_input)


def get_default_playground() -> list[str]:
    return ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)'] 


def draw_current_playground(playground: list[str]) -> None:
    table = rich.table.Table(show_header = False)
    console = rich.console.Console()
    for index in range(0, len(playground), 3):
        table.add_row(playground[index], playground[index+1], playground[index+2])    
    console.print(table)


def ai_makes_first_turn() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(3 + random.randint(0,3))


def main() -> None:
    user_icon, ai_icon = define_icons()
    playground = get_default_playground()
    game_on = True
    clear_screen()
    draw_current_playground(playground)
    print('Game on!', end=' ')
    if ai_makes_first_turn():
        print('AI makes the first turn! Please wait a sec...')
        toggle_ai_brainstorm()
        playground[random.randint(0,8)] = ai_icon
        clear_screen()
        draw_current_playground(playground)
        print('Done! Your turn now...')
    else:
        print('You make the first turn!')
    while game_on:
        user_turn = get_user_turn(playground, user_icon, ai_icon)
        if not user_turn:
            game_on = False
            continue
        playground[user_turn-1] = user_icon
        clear_screen()
        draw_current_playground(playground)
        print('Ok. And now AI will make his turn...')
        toggle_ai_brainstorm()
        clear_screen()
        draw_current_playground(playground)
        print('Done! Your turn now...')
        

if __name__ == '__main__':
    main()
