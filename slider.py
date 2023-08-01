import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider ")
        self.setGeometry(50,50,400,400)
        self.UI()
# dizany elemanlarını yan yan kullanılması için horizontol alt alt ise vertical
    def UI(self):
        verticalBox = QVBoxLayout()
        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter  )
        self.text2 = QLabel("MErhaba")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)
        verticalBox.addStretch()
        verticalBox.addWidget(self.text1)
        verticalBox.addWidget(self.text2)
        verticalBox.addWidget(self.slider)
        self.setLayout(verticalBox)
        self.show()

    def getValue(self):
        self.text1.setText(str(self.slider.value()))
        fontsize = self.slider.value()
        font = QFont("Times", fontsize)
        self.text2.setFont(font )

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()