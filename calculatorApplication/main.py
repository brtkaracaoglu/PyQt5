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
        ##########Entry Field##########
        self.entry_box = QLineEdit(self)
        self.entry_box.resize(335,30)
        self.entry_box.setAlignment(Qt.AlignRight) # LineEdit yazısını sağ taraftan başlattık
        self.entry_box.setStyleSheet("font: 14pt Arial Bold; border: 3px solid gray;"
                                     "border-radius: 5px; background-color: #e6e6fa;")
        self.entry_box.setText("0")
        self.entry_box.move(20,30)
        ##########Number Buttons##########

        btn_number = []
        for i in range(1,10):
            i = QPushButton(str(i), self)
            i.setFont(QFont("Arial", 15))
            i.resize(70,40)
            i.setStyleSheet("background-color: white")
            btn_number.append(i)

        btn_index = 0
        for i in range(0,3):
            for j in range(0,3):
                btn_number[btn_index].move(25+j*90, 70+i*70)
                btn_index += 1
        ##########Operator Buttons##########
        btn_operator = []
        for i in range(4):
            i = QPushButton(self)
            i.resize(70, 40)
            i.setFont(QFont("Arial", 15))
            i.setStyleSheet("background-color: white")
            btn_operator.append(i)
        btn_operator[0].setText("+")
        btn_operator[1].setText("-")
        btn_operator[2].setText("*")
        btn_operator[3].setText("/")
        for i in range(4):
            btn_operator[i].move(290, 70+i*70)



def main():
    App = QApplication(sys.argv)
    window = Calculator()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()