import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("My App")

button1 = QPushButton("Click me")
button1.setStyleSheet("background-color: red; color: white; font-size: 60px;")

button2 = QPushButton("Click me")
button2.setStyleSheet("background-color: blue; color: white; font-size: 30px;")

button3 = QPushButton("Click me")
button3.setStyleSheet("background-color: green; color: white; font-size: 30px;")


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

def slot_example(status_bar):
    status_bar.showMessage("Button clicked", 2000)

status_bar = window.statusBar()
status_bar.showMessage("show message on status bar")

menu = window.menuBar()
first_menu = menu.addMenu("First Menu")
first_action = first_menu.addAction("First Action")
first_action.triggered.connect(lambda: slot_example(status_bar))


window.show()
app.exec()