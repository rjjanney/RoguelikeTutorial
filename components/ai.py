"""AI for the behavior of different classes of opponents."""

import libtcodpy as libtcod


class BasicMonster:
    """Basic monster class."""

    def take_turn(self, target, fov_map, game_map, entities):
        """Do whatever it does in its turn."""
        results = []

        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):

            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)

            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)

        return results
