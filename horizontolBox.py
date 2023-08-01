import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontol Box Layout")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        horizontol = QHBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        horizontol.addStretch()
        horizontol.addWidget(button1)
        horizontol.addWidget(button2)
        horizontol.addWidget(button3)
        horizontol.addStretch()

        self.setLayout(horizontol)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()