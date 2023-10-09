import enum


class Winner(enum.Enum):
    TIE = 'tie'
    USER = 'user'
    AI = 'ai'
    
    def outro_message(self) -> str:
        winner_to_outro_map = {
            'tie' : 'Oops! Game ends with a tie!',
            'user' : 'Congratulations! You win!',
            'ai' : 'Bad news! AI wins!',
        }
        return winner_to_outro_map[self.value]


CLEAR_SCREEN_COMMANDS_MAP = {
    'nt' : 'cls',
    'posix' : 'clear',
}
PLAYABLE_SYMBOLS = ['X', 'O']
PLAYGROUND_ROW_LENGTH = 3
WIN_STREAK = 3
BRAINSTORM_MIN_SEC = 2
BRAINSTORM_MAX_SEC = 4
BRAINSTORM_ERROR_SEC = 0.5
WINNING_MOVE_SKIP_CHANCE = 10
DEFENSIVE_MOVE_SKIP_CHANCE = 25
OFFENSIVE_MOVE_SKIP_CHANCE = 50
