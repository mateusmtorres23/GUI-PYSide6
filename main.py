import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton("Click me")
button.setStyleSheet("background-color: red; color: white; font-size: 30px;")
button.show()

app.exec()