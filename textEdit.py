import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextEdit Kullanımı")
        self.setGeometry(40, 40, 600, 600)
        self.interface()

    def interface(self):
        self.textEdit = QTextEdit(self)
        self.textEdit.move(150, 50)
        #  zengin metini kapattık
        self.textEdit.setAcceptRichText(False)

        self.sendButon = QPushButton("Gönder", self)
        self.sendButon.move(250, 250)
        self.sendButon.clicked.connect(self.getText)

        self.show()

    def getText(self):
        text = self.textEdit.toPlainText()
        print(text)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())