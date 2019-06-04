"""Fighter class is component to keep track of hp etc."""

import tcod as libtcod

from game_messages import Message


class Fighter:
    """Fighter class is component to keep track of hp etc."""

    def __init__(self, hp, defense, power, xp=0):
        """Initialize Fighter class."""
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp

    @property
    def max_hp(self):
        """Take into account equipped item bonuses."""
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        """Take into account equipped item bonuses."""
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

    @property
    def defense(self):
        """Take into account equipped item bonuses."""
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    def take_damage(self, amount):
        """Take damage."""
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        """Heal hp."""
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        """Attack the target."""
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append(
                {'message': Message(
                 '{0} attacks {1} for {2} hit points.'
                 .format(self.owner.name.capitalize(), target.name,
                         str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append(
                {'message':  Message(
                 '{0} attacks {1} but does no damage.'
                 .format(self.owner.name.capitalize(), target.name), libtcod.white)})

        return results
