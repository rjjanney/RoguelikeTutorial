"""Item class for defining properties of items."""


class Item:
    """Item class definition."""

    def __init__(self, use_function=None, **kwargs):
        """Initialize an item instance."""
        self.use_function = use_function
        self.function_kwargs = kwargs
