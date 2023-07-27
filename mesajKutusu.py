import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MessageBox Kullanımı")
        self.setGeometry(40, 40, 400, 400)
        self.interface()

    def interface(self):
        self.exitButon = QPushButton("Çıkış", self)
        self.exitButon.move(150, 100)
        self.exitButon.clicked.connect(self.dialog)

        self.show()

    def dialog(self):
        messageBox = QMessageBox.question(self, "Uyarı !!!", "Çıkmak İstediğinizden Emin Misiniz ?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if messageBox == QMessageBox.Yes:
            sys.exit()
        else:
            print("Çıkış Yapılmadı...")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())