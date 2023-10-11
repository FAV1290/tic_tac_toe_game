from playground import Playground
from ai import ai_makes_a_first_move, output_ai_move
from user_move import fetch_valid_user_move, output_user_move
from win_check import win_check


def output_start_conditions(current_playground: Playground, ai_turn_comes_next: bool) -> None:
    current_playground.draw_layout()
    prompt = ' '.join(
        [
            f'Game on! Your symbol is {current_playground.user_symbol},',
            f'AI symbol is {current_playground.ai_symbol}. Press Enter to continue...'
        ]
    )
    input(prompt)
    if ai_turn_comes_next:
        print('AI makes the first move! Please wait a sec...')
    else:
        print('First move is yours!')
    

def main() -> None:
    current_playground = Playground()
    ai_turn_comes_next = ai_makes_a_first_move()
    output_start_conditions(current_playground, ai_turn_comes_next)
    while current_playground.game_on:
        if ai_turn_comes_next:
            current_playground = output_ai_move(current_playground)
        else:
            user_move = fetch_valid_user_move(current_playground)
            if not user_move:
                current_playground.game_on = False
                continue
            current_playground = output_user_move(current_playground, user_move)
        ai_turn_comes_next = not ai_turn_comes_next
        winner = win_check(current_playground)
        if winner is not None:
            current_playground.draw_layout()
            print(winner.pick_outro_message())
            current_playground.game_on = False


if __name__ == '__main__':
    main()
