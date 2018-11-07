"""Implement the message log. Two classes."""

import libtcodpy as libtcod

import textwrap


class Message:
    """Hold messages for the message log."""

    def __init__(self, text, color=libtcod.white):
        """Initialize the Message class instance."""
        self.text = text
        self.color = color


class MessageLog:
    """Log the messages from the message class here."""

    def __init__(self, x, width, height):
        """Initialize the MessageLog class instance."""
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        """Add a message."""
        # Split the message if necessary, along multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer full, remove first line to make room
            if len(self.messages) == self.height:
                del self.messages[0]

            # Add the new line as a Message object, with the text and the color
            self.messages.append(Message(line, message.color))
