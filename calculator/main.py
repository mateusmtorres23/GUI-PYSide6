import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label = QLabel("Text to test")
    label.setStyleSheet("font-size: 50px;")
    window.addWidgetVLayout(label)
    window.adjustFixedSize()

    window.show()
    app.exec()