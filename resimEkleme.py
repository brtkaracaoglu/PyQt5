import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.interface()
        self.setWindowTitle("Resim Ekleme Kullanımı")
        self.setGeometry(40, 40, 300, 300)

    def interface(self):
        self.QLabel = QLabel("Merhaba Python", self)
        self.QLabel.setFont(font)

        self.image = QLabel(self)
        # setPixmap metodu, etiket nesnesinin içeriğini bir QPixmap nesnesi ile değiştirmek için kullanılır.
        self.image.setPixmap(QPixmap("yaz.jpg"))
        self.image.move(0, 40)


        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())