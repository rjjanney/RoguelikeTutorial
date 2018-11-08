"""Establish game states class to keep track of game states in an enum."""
from enum import Enum, auto


class GameStates(Enum):
    """Enum to keep track of game states."""

    PLAYERS_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    SHOW_INVENTORY = auto()
    DROP_INVENTORY = auto()
    TARGETING = auto()
    LEVEL_UP = auto()
    CHARACTER_SCREEN = auto()
