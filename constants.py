import enum


class Winner(enum.Enum):
    NONE = ''
    TIE = 'Oops! Game ends with a tie!'
    USER = 'Congratulations! You win!'
    AI = 'Bad news! AI wins!'


CLEAR_SCREEN_COMMANDS_MAP = {
    'nt' : 'cls',
    'posix' : 'clear',
}
PLAYABLE_SYMBOLS = ['X', 'O']
PLAYGROUND_ROW_LENGTH = 3
WIN_STREAK = 3
BRAINSTORM_MIN_SEC = 2
BRAINSTORM_MAX_SEC = 5
BRAINSTORM_ERROR_SEC = 0.5
