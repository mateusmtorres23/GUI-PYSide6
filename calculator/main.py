import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
from utils import ICON_PATH, windowsIconVerifier


if __name__ == "__main__":
    windowsIconVerifier() # to change the icon on the taskbar in Windows
    app = QApplication(sys.argv)
    window = MainWindow()


    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label = QLabel("Text to test")
    label.setStyleSheet("font-size: 50px;")
    window.addWidgetVLayout(label)
    window.adjustFixedSize()

    window.show()
    app.exec()