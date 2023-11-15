import enum
import typing
import random


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


class CurrentTurn(enum.IntEnum):
    AI: int = 0
    USER: int = 1

    @classmethod
    def choose_random(cls) -> typing.Self:
        return random.choice(list(cls))

    @classmethod
    def switch_player(cls, instance: typing.Self) -> typing.Self:
        return cls(not instance)
