import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("My App")

        self.button1 = QPushButton("Click me")
        self.button1.setStyleSheet("background-color: red; color: white; font-size: 60px;")
        self.button1.clicked.connect(lambda: self.button_clicked("Red button clicked"))

        self.button2 = QPushButton("Click me")
        self.button2.setStyleSheet("background-color: blue; color: white; font-size: 30px;")
        self.button2.clicked.connect(lambda: self.button_clicked("Blue button clicked"))

        self.button3 = QPushButton("Click me")
        self.button3.setStyleSheet("background-color: green; color: white; font-size: 30px;")
        self.button3.clicked.connect(lambda: self.button_clicked("Green button clicked"))

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.layout.addWidget(self.button1, 1, 1, 1, 1)
        self.layout.addWidget(self.button2, 1, 2, 1, 1)
        self.layout.addWidget(self.button3, 3, 1, 1, 2)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("show message on status bar")

        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu("First Menu")
        self.first_action = self.first_menu.addAction("First Action")
        self.first_action.triggered.connect(self.slot_example)

        self.second_action = self.first_menu.addAction("Second Action")
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.other_slot)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage("first action", 2000)

    @Slot()
    def other_slot(self):
        print(f"Is it checked? {self.second_action.isChecked()}")

    @Slot()
    def button_clicked(self, text):
        self.status_bar.showMessage(text, 3000)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()