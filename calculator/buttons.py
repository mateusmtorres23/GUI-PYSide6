from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QPushButton, QGridLayout
from display import Display, OperationDisplay
from variables import MEDIUM_FONT_SIZE
from utils import isValidNumber
import operator as opr

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
            ['(- )', '0', '.', '='],
        ]
        self.display = display
        self.opDisplay = opDisplay
        self._equation = ""
        self._operator = None
        self._left = None
        self._right = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.opDisplay.setText(value)

    def _makeGrid(self):

        self.display.arrowSignal.connect(self._arrowPressed)
        self.display.delSignal.connect(self.display.backspace)
        self.display.inputSignal.connect(self._insertToDisplay)
        self.display.operatorSignal.connect(self._operatorConfig)
        self.display.eqSignal.connect(self._equalsTo)


        for i, row in enumerate(self._gridMask):
            for j, element in enumerate(row):

                button = Button(element)

                if element not in '0123456789.':
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)


                slot = self._makeButtonSlot(self._insertToDisplay, element)
                self._connectButtonClicked(button, slot)
                self.addWidget(button, i, j, 1, 1)
    
    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            self._connectButtonClicked(button, self._clear)
        
        if text == "◀":
            self._connectButtonClicked(button, self.display.backspace)


        if text in "+-*÷^":
            slot = self._makeButtonSlot(self._operatorConfig, text)
            self._connectButtonClicked(button, slot)
        
        if text == "=":
            slot = self._makeButtonSlot(self._equalsTo)
            self._connectButtonClicked(button, slot)

        if text == "(- )":
            slot = self._makeButtonSlot(self._invertNumber)
            self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _makeButtonSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
    
    @Slot()
    def _operatorConfig(self, text):

        displayText = self.display.text()

        if not isValidNumber(displayText) and self._left is None:
            return

        self.display.clear()

        if displayText:
            self._left = float(displayText)
        
        if self._left.is_integer():
            self._left = int(self._left)

        self._op =  text
        self.equation = f'{self._left} {self._op}'

    @Slot()
    def _invertNumber(self):
        text = self.display.text()

        if not isValidNumber(text):
            return

        number = float(text)
        newNumber = number * -1
        
        if newNumber.is_integer():
            newNumber = int(newNumber)

        self.display.setText(str(newNumber))

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = ""
        self.display.clear()

    @Slot()
    def _equalsTo(self):
        if self._left is None or self._op is None:
            return
        
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._right = float(displayText)
        
        if self._right.is_integer():
            self._right = int(self._right)

        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0

        opMap = {
            '+' : opr.add,
            '-' : opr.sub,
            '*' : opr.mul,
            '÷' : opr.truediv,
            '^' : opr.pow
        }

        try:
            operation = opMap[self._op]
            result = operation(self._left, self._right)
        except ZeroDivisionError:
            self.display.setText("Error")
            print('Zero Division Error')
        
        self.display.clear()
        self.opDisplay.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
    
    @Slot(int)
    def _arrowPressed(self, keyCode):
        KEYS = Qt.Key

        if keyCode == KEYS.Key_Up:
            self.display.setCursorPosition(0)

        elif keyCode == KEYS.Key_Down:
            self.display.setCursorPosition(len(self.display.text()))

        elif keyCode == KEYS.Key_Left:
            self.display.cursorBackward(False)

        elif keyCode == KEYS.Key_Right:
            self.display.cursorForward(False)
