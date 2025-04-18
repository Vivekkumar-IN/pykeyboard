try:
    from telethon import Button
except ImportError:
    Button = None


class InlineKeyboard:
    def __init__(self, row_width=3):
        if Button is None:
            raise ImportError(
                "Telethon module is not installed. Please install it using 'pip install telethon'"
            )

        self.row_width = row_width
        self.inline_keyboard = []

    def add(self, *args):
        self.inline_keyboard.extend(
            [args[i : i + self.row_width] for i in range(0, len(args), self.row_width)]
        )

    def row(self, *args):
        self.inline_keyboard.append([button for button in args])

    def __call__(self):
        return self.inline_keyboard
