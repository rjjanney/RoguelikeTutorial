"""Establish game states class to keep track of game states in an enum."""
from enum import Enum


class GameStates(Enum):
    """Enum to keep track of game states."""

    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    SHOW_INVENTORY = 4
    DROP_INVENTORY = 5
