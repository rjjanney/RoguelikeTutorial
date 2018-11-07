"""Fighter class is component to keep track of hp etc."""

import libtcodpy as libtcod

from game_messages import Message


class Fighter:
    """Fighter class is component to keep track of hp etc."""

    def __init__(self, hp, defense, power):
        """Initialize Fighter class."""
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        """Take damage."""
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

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
