import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Verdana", 12)
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(40, 40, 400, 400)
        self.setWindowTitle("Buton Oluşturma")
        self.interface()

    def interface(self):
        self.QLabel = QLabel("Merhaba Python", self)
        self.QLabel.setFont(font)
        self.QLabel.move(130,40)

        self.buton1 = QPushButton("Giriş", self)
        self.buton1.move(120,80)
        self.buton1.setFont(font)

        self.buton2 = QPushButton("Çıkış", self)
        self.buton2.move(200, 80)
        self.buton2.setFont(font)


        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
