import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(650,150,600,600)
        self.UI()

    def UI(self):
        self.grid = QGridLayout()
        buton1 = QPushButton("Buton 1")
        buton1.clicked.connect(self.clikMe)
        buton2 = QPushButton("Buton 2")
        buton3 = QPushButton("Buton 3")
        buton4 = QPushButton("Buton 4")
        self.grid.addWidget(buton1,0,0)
        self.grid.addWidget(buton2,0,1)
        self.grid.addWidget(buton3,1,0)
        self.grid.addWidget(buton4,1,1)

        self.setLayout(self.grid)

        self .show()

    def clikMe(self):
        print("Merhaba")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()