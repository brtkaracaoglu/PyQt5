import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabWidget(Sekme) ")
        self.setGeometry(650,150,600,600)
        self.UI()
    def UI(self):
        self.tabs = QTabWidget(self)
        self.tabs.resize(600,600)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Birinci Sekme")
        self.tabs.addTab(self.tab2, "İkinci Sekme")
        self.tabs.addTab(self.tab3, "Üçüncü Sekme")

        verticalBox = QVBoxLayout()
        self.text = QLabel("Merhaba")
        self.button = QPushButton("Button")
        self.button.clicked.connect(self.btnFunc)
        verticalBox.addStretch()
        verticalBox.addWidget(self.text)
        verticalBox.addWidget(self.button)
        self.tab1.setLayout(verticalBox)

        self.show()

    def btnFunc(self):
        self.text.setText("Buton çalısıyor..")

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()