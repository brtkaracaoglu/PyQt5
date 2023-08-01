import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
import sqlite3
import personAdd


butonFont = QFont("Arial", 12)
textFont = QFont("Arial", 16)

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

class Person(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)

        self.title = QLabel("Kişilerim", self)
        self.title.setFont(textFont)
        self.title.move(210,70)
        self.title_image = QLabel(self)
        self.title_image.setPixmap(QPixmap("icons/person.png"))
        self.title_image.move(100,40)

        #########################################################
        self.list = QListWidget(self)
        self.list.move(110,100)
        person = cursor.execute("select * from persons")
        for i in person.fetchall():
            self.list.addItem(str(i[0])+ "-" +i[1]+ " " +i[2])

        #########################################################
        self.addButon = QPushButton("Ekle", self)
        self.addButon.setFont(butonFont)
        self.addButon.move(380,100)
        self.addButon.clicked.connect(self.personAdd)

        #########################################################
        self.updateButon = QPushButton("Güncelle", self)
        self.updateButon.setFont(butonFont)
        self.updateButon.move(380,140)
        self.updateButon.clicked.connect(self.personUpdate)

        #########################################################
        self.listButon = QPushButton("Listele", self)
        self.listButon.setFont(butonFont)
        self.listButon.move(380, 180)
        self.listButon.clicked.connect(self.personListing)

        #########################################################
        self.deleteButon = QPushButton("Sil", self)
        self.deleteButon.setFont(butonFont)
        self.deleteButon.move(380, 220)
        self.deleteButon.clicked.connect(self.personDelete)

        #########################################################

        self.show()

    def personAdd(self):
        self.add = personAdd.Add()
        self.add.show()
        self.close()

    def personDelete(self):
         self.person = self.list.currentItem().text()
         id = self.person.split("-")[0]
         self.approval = QMessageBox.question(self, "Uyarı", "Silmek istiyormusunuz ?", QMessageBox.Yes
                                              | QMessageBox.No, QMessageBox.No)
         if (self.approval == QMessageBox.Yes):
             try:
                 cursor.execute("delete from persons where person_id = ? ",(id,))
                 connect.commit()
                 QMessageBox.information(self, "Bilgi", "Kayıt Silindi...")
             except:
                 QMessageBox.information(self, "Hata", "Kayıt Silinemedi...")

             self.close()

    def personUpdate (self):
        self.person = self.list.currentItem().text()
        global  person_id
        person_id = self.person.split("-")[0]

        self.update = Update()
        self.update.show()
        self.close()

    def personListing(self):
        self.person = self.list.currentItem().text()
        global person_id
        person_id = self.person.split("-")[0]

        self.listing = Listing()
        self.listing.show()
        self.close()

class Listing(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Personel Listele")

        try:
            query = cursor.execute("select * from persons where person_id = ?", (person_id,))
            person_information = query.fetchall()
            self.person_id = person_information[0][0]
            self.person_name = person_information[0][1]
            self.person_lastname = person_information[0][2]
            self.person_age = person_information[0][3]
            self.person_address = person_information[0][4]

        except:
            QMessageBox.information(self, "Hata", "...")


        self.title = QLabel("Personel Listele", self)
        self.title.move(210, 40)
        self.title.setFont(textFont)
        self.title_image = QLabel(self)
        self.title_image.setPixmap(QPixmap("icons/update.png"))
        self.title_image.move(140, 5)

        #########################################################
        self.name = QLineEdit(self)
        self.name.move(150, 90)
        self.name.setText(self.person_name)
        self.name.setReadOnly(True)

        #########################################################
        self.lastname = QLineEdit(self)
        self.lastname.move(150, 120)
        self.lastname.setPlaceholderText("Lütfen bir soyisim giriniz")
        self.lastname.setText(self.person_lastname)
        self.lastname.setReadOnly(True)

        #########################################################
        self.age = QComboBox(self)
        self.age.move(150, 150)
        self.age.resize(80, 25)
        for i in range(18, 101):
            self.age.addItem(str(i))
        self.age.setCurrentText(self.person_age)
        self.age.setDisabled(True)

        #########################################################
        self.address = QTextEdit(self)
        self.address.move(150, 180)
        self.address.setText(self.person_address)
        self.address.setReadOnly(True)


        #########################################################

class Update(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Personel Güncelle")

        try:
            query = cursor.execute("select * from persons where person_id = ?", (person_id,))
            person_information = query.fetchall()
            self.person_id = person_information[0][0]
            self.person_name = person_information[0][1]
            self.person_lastname = person_information[0][2]
            self.person_age = person_information[0][3]
            self.person_address = person_information[0][4]

        except:
            QMessageBox.information(self, "Hata", "...")


        self.title = QLabel("Personel Güncelle", self)
        self.title.move(210, 40)
        self.title.setFont(textFont)
        self.title_image = QLabel(self)
        self.title_image.setPixmap(QPixmap("icons/update.png"))
        self.title_image.move(140, 5)

        #########################################################
        self.name = QLineEdit(self)
        self.name.move(150, 90)
        self.name.setText(self.person_name)

        #########################################################
        self.lastname = QLineEdit(self)
        self.lastname.move(150, 120)
        self.lastname.setPlaceholderText("Lütfen bir soyisim giriniz")
        self.lastname.setText(self.person_lastname)

        #########################################################
        self.age = QComboBox(self)
        self.age.move(150, 150)
        self.age.resize(80, 25)
        for i in range(18, 101):
            self.age.addItem(str(i))
        self.age.setCurrentText(self.person_age)

        #########################################################
        self.address = QTextEdit(self)
        self.address.move(150, 180)
        self.address.setText(self.person_address)

        #########################################################
        self.updateButon = QPushButton("Güncelle", self)
        self.updateButon.setFont(butonFont)
        self.updateButon.move(330, 380)
        self.updateButon.clicked.connect(self.personUpdate)
        #########################################################

    def personUpdate(self):
        person_id = self.person_id
        name = self.name.text()
        lastname = self.lastname.text()
        age = self.age.currentText()
        address = self.address.toPlainText()

        try:
            cursor.execute("update persons set name = ?, lastname = ?, age = ?, address = ? where person_id = ?", (name, lastname, age, address, person_id))
            connect.commit()
            QMessageBox.information(self, "Bilgi", "Kişi Güncelledi...")
            self.close()
        except:
            QMessageBox.information(self, "Hata", "Kişi Güncellenmedi...")