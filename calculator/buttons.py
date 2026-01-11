from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from display import Display, OperationDisplay
from variables import MEDIUM_FONT_SIZE
from utils import isValidNumber

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px")
        self.setMinimumSize(60, 60)

class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, opDisplay: OperationDisplay, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '÷'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', None, '.', '='],
        ]
        self.display = display
        self.opDisplay = opDisplay
        self._equation = ""
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.opDisplay.setText(value)

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
                    self._configSpecialButton(button)

                slot = self._makeButtonSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)
                self.addWidget(button, i, j, 1, columnSpan)
    
    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            self._connectButtonClicked(button, self.display.clear)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _makeButtonSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot
                
    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)