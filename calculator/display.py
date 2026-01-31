import operator
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT_SIZE, MINIMUM_WIDHT, TEXT_MARGINS, SMALL_FONT_SIZE
from PySide6.QtGui import QKeyEvent
from utils import isNumOrDot

class Display(QLineEdit):

    inputSignal = Signal(str)
    operatorSignal = Signal(str)
    arrowSignal = Signal(int)
    delSignal = Signal()
    eqSignal = Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumWidth(MINIMUM_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGINS for _ in range(4)])
    
    def keyPressEvent(self, event: QKeyEvent, ):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isArrow = key in [KEYS.Key_Up, KEYS.Key_Down, KEYS.Key_Left, KEYS.Key_Right]
        isOperator = key in [KEYS.Key_P, KEYS.Key_Plus, KEYS.Key_Minus, 
                             KEYS.Key_Asterisk, KEYS.Key_Slash, ]
        isEqual = key in [KEYS.Key_Equal, KEYS.Key_Return]

        if isArrow:
            self.arrowSignal.emit(key)

        if isDelete:
            self.delSignal.emit()

        if isNumOrDot(text):
            self.inputSignal.emit(text)

        if isOperator:
            text = "÷" if text == "/" else text
            self.operatorSignal.emit(text)
        
        if isEqual:
            self.eqSignal.emit()

            
class OperationDisplay(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
