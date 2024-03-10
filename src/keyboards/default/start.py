"""
Inline Keyboards Module.

This module provides a class for generating inline keyboards with various buttons.

Classes:
    InlineKeyboards: Generates inline keyboards with predefined buttons.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class DefaultKeyboards:
    def __init__(self) -> None:
        self.keyboard = ReplyKeyboardMarkup
        self.button = KeyboardButton


    def start_default_keyboard(self) -> ReplyKeyboardMarkup:
        buttons = [
            [
                self.button(text="Start!")
            ]
        ]
        return self.keyboard(keyboard=buttons, resize_keyboard=True)
