import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpinBox Layout")
        self.setGeometry(50,50,400,400)
        self.UI()
# dizany elemanlarını yan yan kullanılması için horizontol alt alt ise vertical
    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(100,50)
        self.spinbox.setRange(25,100)
        #self.spinbox.setMaximum(50)
        self.spinbox.setSingleStep(5)
        self.spinbox.setPrefix("£ ")
        self.spinbox.setSuffix("  cm")
        self.spinbox.valueChanged.connect(self.getValue)

        self.show()
    def getValue(self):
        print(self.spinbox.value())
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()