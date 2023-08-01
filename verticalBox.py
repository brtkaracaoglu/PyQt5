import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(50,50,400,400)
        self.UI()
# dizany elemanlarını yan yan kullanılması için horizontol alt alt ise vertical
    def UI(self):
        vertical = QVBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        vertical.addStretch()
        vertical.addWidget(button1)
        vertical.addWidget(button2)
        vertical.addWidget(button3)
        vertical.addStretch()

        self.setLayout(vertical)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()