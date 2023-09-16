from ai import ai_makes_a_first_move, output_ai_move
from playground import define_symbols, generate_blank_playground, draw_playground
from user_move import fetch_valid_user_move, output_user_move


def output_start_conditions(user_symbol: str, ai_symbol: str) -> list[str]:
    playground = generate_blank_playground()
    draw_playground(playground)
    print(f'Game on! Your symbol is {user_symbol}, AI symbol is {ai_symbol}') 
    if ai_makes_a_first_move():
        print('AI makes the first move! Please wait a sec...')
        playground = output_ai_move(playground, user_symbol, ai_symbol)
    else:
        print('You make the first move!')  
    return playground  


def main() -> None:
    game_on = True  
    user_symbol, ai_symbol = define_symbols()
    playground = output_start_conditions(user_symbol, ai_symbol)
    while game_on:
        user_move = fetch_valid_user_move(playground)
        if not user_move:
            game_on = False
            continue
        playground = output_user_move(playground, user_symbol, user_move)
        playground = output_ai_move(playground, user_symbol, ai_symbol)


if __name__ == '__main__':
    main()
