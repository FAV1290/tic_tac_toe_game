import random
import time


from constants import BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC, PLAYGROUND_SIZE
from playground import draw_playground


def ai_makes_a_first_move() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(random.randint(BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC))


def is_playground_full(playground: list[str], user_symbol: str, ai_symbol: str) -> bool:
    for box in playground:
        if box not in [user_symbol, ai_symbol]:
            return False
    return True


def generate_random_ai_move(playground: list[str], user_symbol: str, ai_symbol: str) -> int | None:
    ai_move = None
    if is_playground_full(playground, user_symbol, ai_symbol):
        return None
    while ai_move is None or playground[ai_move] in [user_symbol, ai_symbol]:
        ai_move = random.randint(0, len(playground) - 1)
    return ai_move


def output_ai_move(playground: list[str], user_symbol: str, ai_symbol: str) -> list[str] | None:
    ai_move = generate_random_ai_move(playground, user_symbol, ai_symbol)
    if ai_move is None: #Or do something else?
        return None
    playground[ai_move] = ai_symbol
    toggle_ai_brainstorm()
    draw_playground(playground)
    print('Done! Your turn now...')
    return playground
