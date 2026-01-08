from PySide6.QtWidgets import QVBoxLayout, QWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle("Calculadora")

    def adjustFixedSize(self):    
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)