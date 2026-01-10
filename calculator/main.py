import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
from utils import windowsIconVerifier
from variables import ICON_PATH
from display import Display, OperationDisplay
from styles import setupTheme
from buttons import Button, ButtonGrid


if __name__ == "__main__":
    windowsIconVerifier() # to change the icon on the taskbar on Windows
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    opDisplay = OperationDisplay("2.00 ^ 10.00 = 1024")
    window.addWidgetVLayout(opDisplay)

    display = Display()
    window.addWidgetVLayout(display)

    buttonGrid = ButtonGrid()
    window.vLayout.addLayout(buttonGrid)

    window.adjustFixedSize()    
    window.show()
    app.exec()