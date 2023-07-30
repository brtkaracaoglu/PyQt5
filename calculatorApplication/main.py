import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(850,200,380,550)
        self.setFixedSize((self.size())) # Kullanıcı ayarladığımız boyutu büyütemesin diye kullanılıyor.
        self.UI()
        self.show()

    def UI(self):
        pass


def main():
    App = QApplication(sys.argv)
    window = Calculator()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()