import enum


class Winner(enum.Enum):
    TIE = 'tie'
    USER = 'user'
    AI = 'ai'

    def pick_outro_message(self) -> str:
        winner_to_outro_map = {
            'tie': 'Oops! Game ends with a tie!',
            'user': 'Congratulations! You win!',
            'ai': 'Bad news! AI wins!',
        }
        return winner_to_outro_map[self.value]
