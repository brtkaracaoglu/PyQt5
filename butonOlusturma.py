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
        self.setWindowTitle("Butonlara Fonksiyon Ekleme")
        self.QLabel = QLabel("Merhaba Python", self)
        self.QLabel.setFont(font)
        self.QLabel.move(130,40)

        self.buton1 = QPushButton("Giriş", self)
        self.buton1.move(120,80)
        self.buton1.setFont(font)
        self.buton1.clicked.connect(self.funcButon1)

        self.buton2 = QPushButton("Çıkış", self)
        self.buton2.move(200, 80)
        self.buton2.setFont(font)
        self.buton2.clicked.connect(self.funcButon2)

        self.show()

    def funcButon1(self):
        self.QLabel.resize(180, 30)
        self.QLabel.setText("Çıkış Butonuna Basıldı")
        self.setWindowTitle("Çıkış butonu aktif")
        self.buton1.close()

    def funcButon2(self):
        self.QLabel.resize(180, 30)
        self.QLabel.setText("Giriş Butonuna Basıldı")
        self.setWindowTitle("Giriş butonu aktif")
        self.buton2.close()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
