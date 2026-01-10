from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px")
        self.setMinimumSize(60, 60)

class ButtonGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '÷'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', None, '.', '='],
        ]
        self._makeGrid()
        self.configStyle()

    def _makeGrid(self):
        zeroSpan = {'0' : 2}

        for i, row in enumerate(self._gridMask):
            for j, element in enumerate(row):

                if element is None:
                    continue

                columnSpan = zeroSpan.get(element, 1)

                button = Button(element)

                if element not in '0123456789.':
                    button.setProperty("cssClass", "specialButton")

                self.addWidget(button, i, j, 1, columnSpan)

    def configStyle(self):
        ...