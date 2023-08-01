import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon
import persons, personAdd

butonFont = QFont("Arial", 12)
textFont = QFont("Arial", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Address Book")
        self.setGeometry(50,50,400,400)
        self.setStyleSheet("background-color: #ccffff")
        self.UI()

    def UI(self):
        self.personsButon = QPushButton("Personel Listesi", self)
        self.personsButon.setStyleSheet("background-color: white")
        self.personsButon.resize(134,25)
        self.personsButon.move(150,50)
        self.personsButon.setFont(butonFont)
        self.personsButon.setIcon(QIcon("icons/person.png"))
        self.personsButon.clicked.connect(self.persons)

        #########################################################
        self.addButon = QPushButton("Personel Ekle", self)
        self.addButon.setStyleSheet("background-color: white")
        self.addButon.resize(134, 25)
        self.addButon.move(150, 100)
        self.addButon.setFont(butonFont)
        self.addButon.setIcon(QIcon("icons/add.png"))
        self.addButon.clicked.connect(self.personAdd)

        #########################################################
        self.aboutButon = QPushButton("Hakkında", self)
        self.aboutButon.setStyleSheet("background-color: white")
        self.aboutButon.resize(134, 25)
        self.aboutButon.move(150, 150)
        self.aboutButon.setFont(butonFont)
        self.aboutButon.setIcon(QIcon("icons/about.png"))

        #########################################################

        self.show()

    def persons(self):
        self.person = persons.Person()
        self.person.show()

    def personAdd(self):
        self.add = personAdd.Add()
        self.add.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
