from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from display import Display
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px")
        self.setMinimumSize(60, 60)

class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '÷'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', None, '.', '='],
        ]
        self.display = display
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

                slot = self._makeButtonSlot(self._buttonTextToDisplay, button)
                button.clicked.connect(slot)
                self.addWidget(button, i, j, 1, columnSpan)

    def _makeButtonSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot
                
    def _buttonTextToDisplay(self, button):
        buttonText = button.text()
        self.display.insert(buttonText)

    def configStyle(self):
        ...