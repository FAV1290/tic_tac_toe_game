import time
import random
import logging
import collections


from game.playground import Playground
from game.ai_tactics import find_notable_indexes
from game.constants import (
    BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC,
    AI_LOGFILE_FILEPATH, AI_LOGGING_FORMAT,
    AI_WIN_SKIP_CHANCE, AI_DEFENCE_SKIP_CHANCE, AI_OFFENCE_SKIP_CHANCE)


logging.basicConfig(filename=AI_LOGFILE_FILEPATH, level=logging.INFO, format=AI_LOGGING_FORMAT)


def ai_makes_a_first_move() -> bool:
    return random.choice([True, False])


def toggle_ai_brainstorm() -> None:
    time.sleep(random.randint(BRAINSTORM_MIN_SEC, BRAINSTORM_MAX_SEC))


def generate_winning_ai_move(playground: Playground) -> int | None:
    winning_indexes = find_notable_indexes(playground)['winning']
    if winning_indexes is None:
        return None
    return collections.Counter(winning_indexes).most_common()[0][0]


def generate_defensive_ai_move(playground: Playground) -> int | None:
    check_breaking_indexes = find_notable_indexes(playground)['defensive']
    if check_breaking_indexes is None:
        return None
    return collections.Counter(check_breaking_indexes).most_common()[0][0]


def generate_offensive_ai_move(playground: Playground) -> int | None:
    suitable_for_offence_indexes = find_notable_indexes(playground)['offensive']
    if suitable_for_offence_indexes is None:
        return None
    return collections.Counter(suitable_for_offence_indexes).most_common()[0][0]


def generate_random_ai_move(playground: Playground) -> int | None:
    ai_move = None
    if playground.is_filled():
        return None
    while ai_move is None or playground.layout[ai_move] in playground.symbols_list():
        ai_move = random.randint(0, playground.row_length ** 2 - 1)
    return ai_move


def is_move_skipped(substitution_chance: int) -> bool:
    return random.randint(1, 100) in range(0, substitution_chance)


def generate_ai_move(playground: Playground) -> int | None:
    winning_move = generate_winning_ai_move(playground)
    if winning_move is not None and not is_move_skipped(AI_WIN_SKIP_CHANCE):
        logging.info(f'MAKING WINNING MOVE, BOX # {playground.layout[winning_move]}')
        return winning_move
    defensive_move = generate_defensive_ai_move(playground)
    if defensive_move is not None and not is_move_skipped(AI_DEFENCE_SKIP_CHANCE):
        logging.info(f'MAKING DEFENSIVE MOVE, BOX # {playground.layout[defensive_move]}')
        return defensive_move
    offensive_move = generate_offensive_ai_move(playground)
    if offensive_move is not None and not is_move_skipped(AI_OFFENCE_SKIP_CHANCE):
        logging.info(f'MAKING OFFENSIVE MOVE, BOX # {playground.layout[offensive_move]}')
        return offensive_move
    logging.info('MAKING RANDOM MOVE')
    return generate_random_ai_move(playground)


def output_ai_move(playground: Playground) -> Playground:
    ai_move = generate_ai_move(playground)
    if ai_move is not None:
        playground.layout[ai_move] = playground.ai_symbol
        toggle_ai_brainstorm()
        playground.draw_layout()
        print('Done! Your turn now...')
    return playground
