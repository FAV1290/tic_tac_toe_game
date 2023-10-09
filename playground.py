import os
import random


from constants import (
    CLEAR_SCREEN_COMMANDS_MAP, PLAYABLE_SYMBOLS, PLAYGROUND_ROW_LENGTH, WIN_STREAK)


class Playground:
    def __init__(
        self,
        row_length = PLAYGROUND_ROW_LENGTH,
        numerate_from = 1,
        win_streak = WIN_STREAK,
    ):
        random.shuffle(PLAYABLE_SYMBOLS)
        self.row_length = row_length
        self.layout = [f'({numerate_from + item})' for item in range(self.row_length ** 2)]
        self.user_symbol, self.ai_symbol = PLAYABLE_SYMBOLS[:2]
        self.game_on = True
        self.win_streak = win_streak
    
    def clear_screen(self) -> None:
        os.system(CLEAR_SCREEN_COMMANDS_MAP.get(os.name, ''))
        
    def draw_layout(self) -> None:
        playground_render = ''
        for index, box in enumerate(self.layout):
            if not index or index % self.row_length == 0:
                playground_render += '\n+' + '───────+' * self.row_length + '\n│'
            playground_render += f'{box:^7}│'    
        #self.clear_screen()
        print(playground_render + '\n+' + '───────+' * self.row_length)

    def symbols_list(self) -> list[str]:
        return [self.user_symbol, self.ai_symbol]
    
    def is_filled(self) -> bool:
        for box in self.layout:
            if box not in self.symbols_list():
                return False
        return True
    
    def is_empty(self) -> bool:
        for symbol in self.symbols_list():
            if self.layout.count(symbol):
                return False
        return True
    
    def rows_indexes_list(self) -> list[list[int]]:
        rows_indexes_list = []
        for start_index in range(0, len(self.layout), self.row_length):
            indexes_row = [i for i in range(start_index, start_index + self.row_length)]
            rows_indexes_list.append(indexes_row)
        return rows_indexes_list
    
    def columns_indexes_list(self) -> list[list[int]]:
        columns_list = []
        for start_index in range(self.row_length):
            column = [i for i in range(start_index, len(self.layout), self.row_length)]
            columns_list.append(column)
        return columns_list    

    def layout_coordinates_list(self) -> list[tuple[int, int]]:
        layout_coordinates, box_x, box_y = [], 0, 0
        for index in range(len(self.layout)):
            layout_coordinates.append((box_x, box_y))
            box_x += 1
            if index and index % self.row_length == self.row_length - 1:  
                box_x = 0
                box_y += 1
        return layout_coordinates

    def diagonals_indexes_list(self) -> list[list[int]]:
        fdiagonals_dict: dict[int, list[int]] = {}
        bdiagonals_dict: dict[int, list[int]] = {}
        for index, coordinates in enumerate(self.layout_coordinates_list()):
            xy_sum = coordinates[0] + coordinates[1]
            xy_diff = coordinates[0] - coordinates[1]
            fdiagonals_dict[xy_sum] = fdiagonals_dict.get(xy_sum, []) + [index]
            bdiagonals_dict[xy_diff] = bdiagonals_dict.get(xy_diff, []) + [index]
        diagonals_list = list(fdiagonals_dict.values()) + list(bdiagonals_dict.values())
        return diagonals_list
