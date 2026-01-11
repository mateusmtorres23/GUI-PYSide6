from PySide6.QtWidgets import QLabel, QLineEdit, QWidget
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, MINIMUM_WIDHT, TEXT_MARGINS, SMALL_FONT_SIZE

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumWidth(MINIMUM_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGINS for _ in range(4)])

class OperationDisplay(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
