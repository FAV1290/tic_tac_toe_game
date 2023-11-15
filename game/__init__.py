from game.enums import CurrentTurn
from game.win_check import win_check
from game.playground import Playground
from game.ai_move import output_ai_move
from game.user_move import fetch_valid_user_move, output_user_move


class TicTacToeGame:
    def __init__(self) -> None:
        self.playground: Playground = Playground()
        self.current_turn: CurrentTurn = CurrentTurn.choose_random()
        self.game_on = True

    def print_start_conditions(self) -> None:
        self.playground.draw_layout()
        prompt = ' '.join(
            [
                f'Game on! Your symbol is {self.playground.user_symbol},',
                f'AI symbol is {self.playground.ai_symbol}. Press Enter to continue...'
            ]
        )
        input(prompt)
        if self.current_turn == CurrentTurn.AI:
            print('AI makes the first move! Please wait a sec...')
        else:
            print('First move is yours!')

    def run(self) -> None:
        self.print_start_conditions()
        while self.game_on:
            if self.current_turn == CurrentTurn.AI:
                self.playground = output_ai_move(self.playground)
            else:
                user_move = fetch_valid_user_move(self.playground)
                if not user_move:
                    self.game_on = False
                    continue
                self.playground = output_user_move(self.playground, user_move)
            self.current_turn = CurrentTurn.switch_player(self.current_turn)
            winner = win_check(self.playground)
            if winner:
                self.playground.draw_layout()
                print(winner.pick_outro_message())
                self.game_on = False
