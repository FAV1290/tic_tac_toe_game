from playground import Playground
from ai import ai_makes_a_first_move, output_ai_move
from user_move import fetch_valid_user_move, output_user_move


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
        if current_playground.is_filled():
            current_playground.draw_layout()
            print('Game ends with a tie!')
            current_playground.game_on = False
            continue
        elif ai_turn_comes_next:
            current_playground = output_ai_move(current_playground)
        else:
            user_move = fetch_valid_user_move(current_playground)
            if not user_move:
                current_playground.game_on = False
                continue
            current_playground = output_user_move(current_playground, user_move)
        ai_turn_comes_next = not ai_turn_comes_next


if __name__ == '__main__':
    main()
