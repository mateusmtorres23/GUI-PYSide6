import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

button1 = QPushButton("Click me")
button1.setStyleSheet("background-color: red; color: white; font-size: 60px;")

button2 = QPushButton("Click me")
button2.setStyleSheet("background-color: blue; color: white; font-size: 30px;")

button3 = QPushButton("Click me")
button3.setStyleSheet("background-color: green; color: white; font-size: 30px;")

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)


layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show()

app.exec()