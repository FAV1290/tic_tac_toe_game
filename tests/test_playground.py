from playground import Playground


def test_is_filled() -> None:
    playground = Playground(row_length=3)
    layouts_and_results = [
        (['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)'], False),
        ([playground.ai_symbol] * 9, True),
        ([playground.user_symbol] * 9, True),
        ([playground.ai_symbol] * 5 + [playground.user_symbol] * 4, True),
        (['(1)', '(2)', '(3)', playground.ai_symbol, '(5)', '(6)', '(7)', '(8)', '(9)'], False),
        (['(1)', '(2)', '(3)', playground.user_symbol, '(5)', '(6)', '(7)', '(8)', '(9)'], False),
        (['(1)', '(2)', '(3)', '(4)'], False),
    ]
    for layout, test_result in layouts_and_results:
        playground.layout = layout
        playground.row_length = len(playground.layout) ** 0.5
        assert playground.is_filled() == test_result


def test_is_empty() -> None:
    playground = Playground(row_length=3)
    layouts_and_results = [
        (['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)'], True),
        ([playground.ai_symbol] * 9, False),
        ([playground.user_symbol] * 9, False),
        ([playground.ai_symbol] * 5 + [playground.user_symbol] * 4, False),
        (['(1)', '(2)', '(3)', playground.ai_symbol, '(5)', '(6)', '(7)', '(8)', '(9)'], False),
        (['(1)', '(2)', '(3)', playground.user_symbol, '(5)', '(6)', '(7)', '(8)', '(9)'], False),
        (['(1)', '(2)', '(3)', '(4)'], True),
    ]
    for layout, test_result in layouts_and_results:
        playground.layout = layout
        playground.row_length = len(playground.layout) ** 0.5
        assert playground.is_empty() == test_result    


def test_rows_indexes_list() -> None:
    row_length_to_rows_indexes_map = {
        2: [[0, 1], [2, 3]],
        3: [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        4: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],    
    }
    for row_length, correct_rows_indexes_list in row_length_to_rows_indexes_map.items():
        test_playground = Playground(row_length=row_length)
        assert test_playground.rows_indexes_list() == correct_rows_indexes_list


def test_columns_indexes_list() -> None:
    row_length_to_columns_indexes_map = {
        2: [[0, 2], [1, 3]],
        3: [[0, 3, 6], [1, 4, 7], [2, 5, 8]],
        4: [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]],  
    }
    for row_length, correct_columns_indexes_list in row_length_to_columns_indexes_map.items():
        test_playground = Playground(row_length=row_length)
        assert test_playground.columns_indexes_list() == correct_columns_indexes_list


def test_layout_coordinates_list() -> None:
    row_length_to_layout_coordinates_map = {
        2: [(0, 0), (1, 0), (0, 1), (1,1)],
        3: [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)],
        4: [
            (0, 0), (1, 0), (2, 0), (3, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),
            (0, 3), (1, 3), (2, 3), (3, 3),
        ],
    }   
    for row_length, correct_coordinates_list in row_length_to_layout_coordinates_map.items():
        test_playground = Playground(row_length=row_length)
        assert test_playground.layout_coordinates_list() == correct_coordinates_list


def test_diagonals_indexes_list() -> None:
    row_length_to_diagonals_indexes_map = {
        2: [[0], [1, 2], [3], [0, 3], [1], [2]],
        3: [[0], [1, 3], [2, 4, 6], [5, 7], [8], [0, 4, 8], [1, 5], [2], [3, 7], [6]],
        4: [
            [0], [1, 4], [2, 5, 8], [3, 6, 9, 12], [7, 10, 13], [11, 14], [15],
            [0, 5, 10, 15], [1, 6, 11], [2, 7], [3], [4, 9, 14], [8, 13], [12],
        ]
    }
    for row_length, correct_diagonals_indexes_list in row_length_to_diagonals_indexes_map.items():
        test_playground = Playground(row_length=row_length)
        assert test_playground.diagonals_indexes_list() == correct_diagonals_indexes_list
