"""Item class for defining properties of items."""


class Item:
    """Item class definition."""

    def __init__(self, use_function=None, targeting=False,
                 targeting_message=None, **kwargs):
        """Initialize an item instance."""
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.function_kwargs = kwargs
