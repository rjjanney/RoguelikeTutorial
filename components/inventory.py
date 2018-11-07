"""Inventory class. Helper class for keeping track of items player has."""

import libtcodpy as libtcod

from game_messages import Message


class Inventory:
    """Inventory class definition."""

    def __init__(self, capacity):
        """Initialize Inventory instance with capacity."""
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        """Generate add item message when item picked up."""
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You can\'t carry any more. Inventory full',
                                   libtcod.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}!'.format(item.name),
                                   libtcod.blue)
            })

            self.items.append(item)

        return results

    def use(self, item_entity, **kwargs):
        """Use an item from inventory."""
        results = []

        item_component = item_entity.item

        if item_component.use_function is None:
            results.append({
                'message': Message('The {0} cannot be used'.format(
                    item_entity.name), libtcod.yellow)
            })
        else:
            kwargs = {**item_component.function_kwargs, **kwargs}
            item_use_results = item_component.use_function(self.owner,
                                                           **kwargs)

            for item_use_result in item_use_results:
                if item_use_result.get('consumed'):
                    self.remove_item(item_entity)

            results.extend(item_use_results)

        return results

    def remove_item(self, item):
        """Remove item."""
        self.items.remove(item)

    def drop_item(self, item):
        """Drop item."""
        results = []

        item.x = self.owner.x
        item.y = self.owner.y

        self.remove_item(item)
        results.append({
            'item_dropped': item,
            'message': Message('You dropped {0}'.format(item.name),
                               libtcod.yellow)
        })

        return results
