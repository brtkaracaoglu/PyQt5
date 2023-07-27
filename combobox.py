import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox Kullanımı")
        self.setGeometry(40, 40, 400, 400)
        self.interface()

    def interface(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItems(["Veli", "Mehmet", "Ali"])

        liste = ["Zeynep", "Aslı", "Funda", "Fadik"]

        for i in liste:
            self.combo.addItem(i)

        for i in range(18, 51):
            self.combo.addItem(str(i))
        self.combo.activated.connect(self.comboFunc)

        self.saveButon = QPushButton("Kaydet", self)
        self.saveButon.move(250, 100)
        self.saveButon.clicked.connect(self.saveButonFunc)


        self.show()

    def comboFunc(self):
        text = str(self.combo.currentText())
        print(text)

    def saveButonFunc(self):
        text = str(self.combo.currentText())
        print(text)



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())