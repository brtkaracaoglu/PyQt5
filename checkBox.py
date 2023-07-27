import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.interface()
        self.setWindowTitle("CheckBox Kullanımı")
        self.setGeometry(40, 40, 300, 300)

    def interface(self):
        self.nameBox = QLineEdit(self)
        self.nameBox.setPlaceholderText("Lütfen İsminizi Giriniz")
        self.nameBox.move(80, 40)

        self.lastnameBox = QLineEdit(self)
        self.lastnameBox.setPlaceholderText("Lütfen Soyisminizi Giriniz")
        self.lastnameBox.move(80, 70)

        self.man = QCheckBox("Erkek", self)
        self.man.move(80, 90)

        self.woman = QCheckBox("Kadın", self)
        self.woman.move(150, 90)

        self.saveButon = QPushButton("Kaydet", self)
        self.saveButon.move(100, 120)
        self.saveButon.clicked.connect(self.save)


        self.show()

    def save(self):
        if (self.man.isChecked()):
            print("İsminiz :" + self.nameBox.text() + "\n Soyisminiz : " + self.lastnameBox.text() + "\n Cinsiyetiniz : Erkek")
        else:
            print("İsminiz :" + self.nameBox.text() + "\n Soyisminiz : " + self.lastnameBox.text() + "\n Cinsiyetiniz : Kadın")



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())