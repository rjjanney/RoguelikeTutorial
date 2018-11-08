"""Player's accumulated experience points, broken down into levels."""


class Level:
    """Level class. Incremented by passing xp thresholds."""

    def __init__(
            self, current_level=1, current_xp=0, level_up_base=200,
            level_up_factor=150):
        """Initialize Level instance."""
        self.current_level = current_level
        self.current_xp = current_xp
        self.level_up_base = level_up_base
        self.level_up_factor = level_up_factor

    @property
    def experience_to_next_level(self):
        """Return XP needed to attain next level."""
        return self.level_up_base + self.current_level * self.level_up_factor

    def add_xp(self, xp):
        """Add xp to current xp. Returns true if player levels up."""
        self.current_xp += xp

        if self.current_xp > self.experience_to_next_level:
            self.current_xp -= self.experience_to_next_level
            self.current_level += 1

            return True

        else:
            return False

