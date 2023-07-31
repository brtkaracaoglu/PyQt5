import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
import sqlite3

butonFont = QFont("Arial", 12)
textFont = QFont("Arial", 16)

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Personel Ekle")

        self.title = QLabel("Personel Ekle", self)
        self.title.move(210,40)
        self.title.setFont(textFont)
        self.title_image = QLabel(self)
        self.title_image.setPixmap(QPixmap("icons/add.png"))
        self.title_image.move(140,5)

        #########################################################
        self.name = QLineEdit(self)
        self.name.move(150,90)
        self.name.setPlaceholderText("Lütfen bir isim giriniz")

        #########################################################
        self.lastname = QLineEdit(self)
        self.lastname.move(150,120)
        self.lastname.setPlaceholderText("Lütfen bir soyisim giriniz")

        #########################################################
        self.age = QComboBox(self)
        self.age.move(150,150)
        self.age.resize(80,25)
        for i in range(18,101):
            self.age.addItem(str(i))

        #########################################################
        self.address = QTextEdit(self)
        self.address.move(150,180)

        #########################################################
        self.addButon = QPushButton("Ekle", self)
        self.addButon.setFont(butonFont)
        self.addButon.move(330,380)
        self.addButon.clicked.connect(self.add)

        #########################################################

    def add(self):
        name = self.name.text()
        lastname = self.lastname.text()
        age = self.age.currentText()
        address = self.address.toPlainText()
        if (name and lastname and address !=""):

            try:
                cursor.execute("insert into persons (name,lastname,age,address) values (?,?,?,?)", (name,lastname,age,address))
                connect.commit()
                QMessageBox.information(self, "Bilgi", "Veriler Eklendi...")
                self.name.setText("")
                self.lastname.setText("")
                self.age.setCurrentIndex(0)
                self.address.setText("")
            except:
                QMessageBox.information(self, "Hata", "Veriler Eklenmedi...")
        else:
            QMessageBox.information(self, "Hata", "Alanlar Boş Olamaz...")
