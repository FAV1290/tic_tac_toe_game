import os
import random


from constants import CLEAR_SCREEN_COMMANDS_MAP, PLAYABLE_SYMBOLS, PLAYGROUND_SIZE


def clear_screen() -> None:
    os.system(CLEAR_SCREEN_COMMANDS_MAP.get(os.name, ''))


def define_symbols() -> tuple[str, str]:
    random.shuffle(PLAYABLE_SYMBOLS)
    user_symbol, ai_symbol = PLAYABLE_SYMBOLS[:2]
    return user_symbol, ai_symbol


def generate_blank_playground() -> list[str]:
    blank_playground = []
    for item in range(PLAYGROUND_SIZE ** 2):
        blank_playground.append(f'({item + 1})')
    return blank_playground


def draw_playground(playground: list[str]) -> None:
    playground_render = ''
    for index, box in enumerate(playground):
        if not index or index % PLAYGROUND_SIZE == 0:
            playground_render += '\n+' + '───────+' * PLAYGROUND_SIZE + '\n│'
        playground_render += f'{box:^7}│'    
    clear_screen()    
    print(playground_render + '\n+' + '───────+' * PLAYGROUND_SIZE)
    