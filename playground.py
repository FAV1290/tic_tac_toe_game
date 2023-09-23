import os
import random


from constants import CLEAR_SCREEN_COMMANDS_MAP, PLAYABLE_SYMBOLS, PLAYGROUND_ROW_LENGTH


class Playground:
    def __init__(
        self,
        row_length = PLAYGROUND_ROW_LENGTH,
        numerate_from = 1
    ):
        random.shuffle(PLAYABLE_SYMBOLS)
        self.row_length = row_length
        self.layout = [f'({numerate_from + item})' for item in range(self.row_length ** 2)]
        self.user_symbol, self.ai_symbol = PLAYABLE_SYMBOLS[:2]
        self.game_on = True
    
    def clear_screen(self) -> None:
        os.system(CLEAR_SCREEN_COMMANDS_MAP.get(os.name, ''))
        
    def draw_layout(self) -> None:
        playground_render = ''
        for index, box in enumerate(self.layout):
            if not index or index % self.row_length == 0:
                playground_render += '\n+' + '───────+' * self.row_length + '\n│'
            playground_render += f'{box:^7}│'    
        self.clear_screen()
        print(playground_render + '\n+' + '───────+' * self.row_length)

    def symbols_list(self) -> list[str]:
        return [self.user_symbol, self.ai_symbol]
    
    def is_filled(self) -> bool:
        for box in self.layout:
            if box not in self.symbols_list():
                return False
        return True
