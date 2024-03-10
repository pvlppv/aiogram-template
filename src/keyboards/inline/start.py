"""
Inline Keyboards Module.

This module provides a class for generating inline keyboards with various buttons.

Classes:
    InlineKeyboards: Generates inline keyboards with predefined buttons.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = InlineKeyboardMarkup
        self.button = InlineKeyboardButton


    def start_inline_keyboard(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Start!", callback_data="start")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
