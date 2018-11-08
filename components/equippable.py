"""Items that can be equipped."""

class Equippable:
    """Class of objects that can be equipped."""

    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0):
        """Initialize instance equippable class."""
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
