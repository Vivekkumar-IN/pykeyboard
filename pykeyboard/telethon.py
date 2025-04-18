try:
    from telethon import Button
    from telethon.tl.types import KeyboardButtonRow, ReplyInlineMarkup, KeyboardButton

    imported = True
except ImportError:
    imported = None


class InlineKeyboard:
    def __init__(self, row_width=3, raw_buttons=None):
        if imported is None:
            raise ImportError(
                "Telethon module is not installed. Please install it using 'pip install telethon'"
            )

        self.row_width = row_width
        self.inline_keyboard = []
        self.raw_buttons = raw_buttons

    def add(self, *args):
        self._check_buttons(args)
        self.inline_keyboard.extend(
            [args[i : i + self.row_width] for i in range(0, len(args), self.row_width)]
        )

    def row(self, *args):
        self._check_buttons(args)
        self.inline_keyboard.append([button for button in args])

    def __call__(self):
        if self.raw_buttons:
            rows = [KeyboardButtonRow(buttons=row) for row in self.inline_keyboard]
            return ReplyInlineMarkup(rows=rows)
        return self.inline_keyboard

    def _check_buttons(self, buttons):
        if not buttons:
            return

        btn_type = self._get_button_type(buttons[0])

        if self.raw_buttons is None:
            self.raw_buttons = btn_type == "raw"
        else:
            expected = "raw" if self.raw_buttons else "custom"
            if btn_type != expected:
                raise TypeError(f"Mismatched button type: expected {expected} buttons.")

        for btn in buttons:
            if self._get_button_type(btn) != btn_type:
                raise TypeError(
                    "Do not mix custom Button and raw button types in the same keyboard."
                )

    def _get_button_type(self, button):
        if isinstance(button, Button):
            return "custom"
        if KeyboardButton.SUBCLASS_OF_ID == button.SUBCLASS_OF_ID:
            return "raw"
        return "unknown"
