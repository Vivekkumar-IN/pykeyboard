try:
    from telethon.tl.types import KeyboardButtonRow, ReplyInlineMarkup
except ImportError:
    ReplyInlineMarkup = KeyboardButtonRow = None


class InlineKeyboard(ReplyInlineMarkup):
    def __init__(self, row_width=3):
        self.row_width = row_width
        self.rows = []
        if KeyboardButtonRow and ReplyInlineMarkup is None:
            raise ImportError(
                "Telethon module is not installed. Please install it using 'pip install telethon'"
            )

    def add(self, *args):
        self._check_buttons(args)
        for i in range(0, len(args), self.row_width):
            row = args[i : i + self.row_width]
            self.rows.append(KeyboardButtonRow(buttons=list(row)))

    def row(self, *args):
        self._check_buttons(args)
        self.rows.append(KeyboardButtonRow(buttons=list(args)))

    def _check_buttons(self, buttons):
        for btn in buttons:
            if getattr(btn, "SUBCLASS_OF_ID", None) != 0xBAD74A3:
                raise TypeError("TODO")
