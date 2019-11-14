import sys
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import random, copy

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.title = 'Жёлтые окружности'
        self.draw = None
        self.InitWindow()

    def InitWindow(self):
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
            rad = random.randrange(255)
            x = random.randrange(255)
            y = random.randrange(255)
            qp.drawEllipse(x, y, rad, rad)
            qp.end()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())