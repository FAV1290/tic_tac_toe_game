from ai import ai_makes_a_first_move, output_ai_move, is_playground_full
from playground import define_symbols, generate_blank_playground, draw_playground
from user_move import fetch_valid_user_move, output_user_move


def output_start_conditions(
    playground: list[str], 
    user_symbol: str, 
    ai_symbol: str, 
    ai_turn_comes_next: bool
) -> None:
    draw_playground(playground)
    input(f'Game on! Your symbol is {user_symbol}, AI symbol is {ai_symbol}. Press Enter to continue...')
    if ai_turn_comes_next:
        print('AI makes the first move! Please wait a sec...')
    else:
        print('First move is yours!')
    

def main() -> None:
    game_on = True  
    user_symbol, ai_symbol = define_symbols()
    playground = generate_blank_playground()
    ai_turn_comes_next = ai_makes_a_first_move()
    output_start_conditions(playground, user_symbol, ai_symbol, ai_turn_comes_next)
    while game_on:
        if is_playground_full(playground, user_symbol, ai_symbol):
            new_playground = None
        elif ai_turn_comes_next:
            new_playground = output_ai_move(playground, user_symbol, ai_symbol)
        else:
            user_move = fetch_valid_user_move(playground)
            if not user_move:
                game_on = False
                continue
            new_playground = output_user_move(playground, user_symbol, user_move)
        try:
            assert new_playground
            playground = new_playground
        except AssertionError:
            draw_playground(playground)
            print('Game ends with a tie!')
            game_on = False
        ai_turn_comes_next = not ai_turn_comes_next 


if __name__ == '__main__':
    main()
