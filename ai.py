import random
import time


from constants import BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC
from playground import Playground


def ai_makes_a_first_move() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(random.randint(BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC))


def generate_random_ai_move(playground: Playground) -> int | None:
    ai_move = None
    if playground.is_filled():
        return None
    while ai_move is None or playground.layout[ai_move] in playground.symbols_list():
        ai_move = random.randint(0, playground.row_length ** 2 - 1)
    return ai_move


def output_ai_move(playground: Playground) -> Playground:
    ai_move = generate_random_ai_move(playground)
    if ai_move is not None:
        playground.layout[ai_move] = playground.ai_symbol
        toggle_ai_brainstorm()
        playground.draw_layout()
        print('Done! Your turn now...')
    return playground
