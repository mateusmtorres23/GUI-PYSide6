from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px")
        self.setMinimumSize(60, 60)
        self.setProperty("cssClass", "specialButton")

class ButtonGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        ...