import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.interface()
        self.setWindowTitle("Line Edit Kullanımı")
        self.setGeometry(40, 40, 300, 300)


    def interface(self):
        self.QLabel = QLabel("", self)
        self.QLabel.move(40, 20) # konumu ayarlıyoruz QLabel ın
        self.QLabel.resize(200, 20)

        self.nameBox = QLineEdit(self)
        self.nameBox.move(80, 40)
        # kullanıcının giriş kutusuna bir ipucu metni (placeholder text) sağlamak için kullanılır.
        self.nameBox.setPlaceholderText("Lütfen isminizi giriniz")

        self.passwordBox = QLineEdit(self)
        self.passwordBox.move(80, 80)
        self.passwordBox.setPlaceholderText("Lütfen şifrenizi giriniz")
        # metni şifreli metin olarak görüntülemek için kullanılır.
        self.passwordBox.setEchoMode(QLineEdit.Password)

        self.saveButon = QPushButton("Kaydet", self)
        self.saveButon.move(110, 110)
        self.saveButon.clicked.connect(self.save)

        self.show()

    def save(self):
        self.name = self.nameBox.text()
        self.password = self.passwordBox.text()
        self.QLabel.setText("İsminiz :"+ self.name + " " + "Şifreniz :"+ self.password)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())