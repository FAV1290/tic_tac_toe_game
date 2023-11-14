from game.playground import Playground


def sum_playground_elements_indexes_lists(playground: Playground) -> list[list[int]]:
    rows_indexes = playground.rows_indexes_list()
    columns_indexes = playground.columns_indexes_list()
    diagonals_indexes = playground.diagonals_indexes_list()
    overall_elements_indexes = rows_indexes + columns_indexes + diagonals_indexes
    return overall_elements_indexes


def create_win_streak_slices_list(playground: Playground) -> list[list[int]]:
    win_streak = playground.win_streak
    win_streak_slices = []
    playground_elements = sum_playground_elements_indexes_lists(playground)
    for playground_element in playground_elements:
        if len(playground_element) < win_streak:
            continue
        for start_index in range(0, len(playground_element) - win_streak + 1):
            win_streak_slices.append(playground_element[start_index:start_index + win_streak])
    return win_streak_slices


def filter_blank_boxes_indexes(playground: Playground, slice: list[int]) -> list[int]:
    return [index for index in slice if playground.layout[index] not in playground.symbols_list()]


def find_winning_indexes(
    playground: Playground,
    slice: list[int],
    filled_by_user: int,
    filled_by_ai: int,
) -> list[int] | None:
    winning_indexes = None
    if not filled_by_user and filled_by_ai == playground.win_streak - 1:
        winning_indexes = filter_blank_boxes_indexes(playground, slice)
    return winning_indexes


def find_check_breaking_indexes(
    playground: Playground,
    slice: list[int],
    filled_by_user: int,
    filled_by_ai: int,
) -> list[int] | None:
    check_breaking_indexes = None
    if not filled_by_ai and filled_by_user == playground.win_streak - 1:
        check_breaking_indexes = filter_blank_boxes_indexes(playground, slice)
    return check_breaking_indexes


def find_suitable_for_offence_indexes_in_slice(
    playground: Playground,
    slice: list[int],
    filled_by_user: int,
) -> list[int] | None:
    offensive_indexes = None
    if not filled_by_user:
        offensive_indexes = filter_blank_boxes_indexes(playground, slice)
    return offensive_indexes


def find_notable_indexes(playground: Playground) -> dict[str, list[int] | None]:
    notable_indexes: dict[str, list[int] | None] = {
        'offensive': [],
        'defensive': [],
        'winning': [],
    }
    for slice in create_win_streak_slices_list(playground):
        slice_layout = list(map(lambda index: playground.layout[index], slice))
        filled_by_user = slice_layout.count(playground.user_symbol)
        filled_by_ai = slice_layout.count(playground.ai_symbol)
        slice_winning_indexes = find_winning_indexes(
            playground, slice, filled_by_user, filled_by_ai)
        slice_check_breaking_indexes = find_check_breaking_indexes(
            playground, slice, filled_by_user, filled_by_ai)
        slice_offensive_indexes = find_suitable_for_offence_indexes_in_slice(
            playground, slice, filled_by_user)
        if notable_indexes['winning'] is not None and slice_winning_indexes is not None:
            notable_indexes['winning'] += slice_winning_indexes
        if notable_indexes['defensive'] is not None and slice_check_breaking_indexes is not None:
            notable_indexes['defensive'] += slice_check_breaking_indexes
        if notable_indexes['offensive'] is not None and slice_offensive_indexes is not None:
            notable_indexes['offensive'] += slice_offensive_indexes
    for move_type, indexes_list in notable_indexes.items():
        if not indexes_list:
            notable_indexes[move_type] = None
    return notable_indexes
