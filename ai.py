import random
import time


from constants import BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC, PLAYGROUND_SIZE
from playground import draw_playground


def ai_makes_a_first_move() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(random.randint(BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC))


def generate_random_ai_move(playground: list[str], user_symbol: str, ai_symbol: str) -> int:
    ai_move = None
    while ai_move is None or playground[ai_move] in [user_symbol, ai_symbol]:
        ai_move = random.randint(0, PLAYGROUND_SIZE ** 2 - 1)
    return ai_move


def output_ai_move(playground: list[str], user_symbol: str, ai_symbol: str) -> list[str]:
    ai_move = generate_random_ai_move(playground, user_symbol, ai_symbol)
    playground[ai_move] = ai_symbol
    toggle_ai_brainstorm()
    draw_playground(playground)
    print('Done! Your turn now...')
    return playground
