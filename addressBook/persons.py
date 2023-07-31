import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap

butonFont = QFont("Arial", 12)
textFont = QFont("Arial", 16)


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

        #########################################################
        self.addButon = QPushButton("Ekle", self)
        self.addButon.setFont(butonFont)
        self.addButon.move(380,100)

        #########################################################
        self.updateButon = QPushButton("Güncelle", self)
        self.updateButon.setFont(butonFont)
        self.updateButon.move(380,140)

        #########################################################
        self.listButon = QPushButton("Listele", self)
        self.listButon.setFont(butonFont)
        self.listButon.move(380, 180)

        #########################################################
        self.deleteButon = QPushButton("Sil", self)
        self.deleteButon.setFont(butonFont)
        self.deleteButon.move(380, 220)

        #########################################################

