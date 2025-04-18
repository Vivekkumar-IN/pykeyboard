try:
    from telethon import Button
    from telethon.tl.types import KeyboardButtonRow, ReplyInlineMarkup
    imported = True
except ImportError:
    imported = None


class InlineKeyboard:
    def __init__(self, row_width=3):
        if imported is None:
            raise ImportError(
                "Telethon module is not installed. Please install it using 'pip install telethon'"
            )

        self.row_width = row_width
        self.inline_keyboard = []

    def add(self, *args):
        self._check_buttons(args)
        self.inline_keyboard.extend(
            [list(args[i : i + self.row_width]) for i in range(0, len(args), self.row_width)]
        )

    def row(self, *args):
        self._check_buttons(args)
        self.inline_keyboard.append([button for button in args])

    def __call__(self):
        rows = [KeyboardButtonRow(buttons=row) for row in self.inline_keyboard]
        return ReplyInlineMarkup(rows=rows)

    def _check_buttons(self, buttons):
        for btn in buttons:
            if not hasattr(btn, "SUBCLASS_OF_ID") or btn.SUBCLASS_OF_ID != 0xbad74a3:
                raise TypeError(
                    "TODO"
                )